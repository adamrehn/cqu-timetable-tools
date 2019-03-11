from .MalformedResultError import MalformedResultError
import itertools, re, requests
from bs4 import BeautifulSoup

class Timetable(object):
	'''
	Provides functionality for parsing CQU Timetable data
	'''
	
	@staticmethod
	def get_events(campus, term, subjects):
		'''
		Retrieves the timetable events for the specified subjects
		'''
		
		# Retrieve the list of timetable events for our selected subjects
		response = requests.post('https://handbook.cqu.edu.au/facet/timetables/search-timetable', data = {
			'term': 'T{}'.format(term),
			'location': campus.upper(),
			'unitCode[]': [code.upper() for code in subjects]
		})
		
		# Iterate over the entries in the HTML response and extract the event details
		events = []
		html = BeautifulSoup(response.text, 'html.parser')
		for entry in html.select('.mc-card-blue'):
			
			# Create an object to hold the parsed details
			details = {}
			
			# Retrieve the header details for the entry and verify that we have two fields
			header = entry.select('.mc-card-header .row > *:first-child')
			if len(header) != 2:
				raise MalformedResultError
			
			# Verify that the entry header contains a subject identifier
			headerDetails = header[0].get_text()
			headerDetails = re.search('(\w+)\s+([\w| ]+)', headerDetails)
			if headerDetails is None:
				raise MalformedResultError
			
			# Extract the subject code and name from the identifier
			details['code'] = headerDetails.group(1)
			details['name'] = headerDetails.group(2)
			
			# Extract the event type (lecture, tutorial, etc.)
			details['type'] = header[1].get_text().strip()
			
			# Retrieve the body details for the entry and verify that we have 8 fields
			body = entry.select('.mc-card-body .col-xl-3')
			fields = [field.get_text().strip() for field in body]
			if len(fields) != 8:
				raise MalformedResultError
			
			# Extract the location and day of the week
			details['location'] = fields[2]
			details['day'] = fields[4]
			
			# Extract the start time and end time
			details['start'], details['end'] = Timetable._splitAndVerify(fields[5], ' - ', 2)
			
			# Extract the list of weeks, expanding any ranges
			weekRanges = fields[7].replace('Weeks: ', '').split(', ')
			details['weeks'] = list(itertools.chain.from_iterable([
				Timetable._expandRange(w) for w in weekRanges
			]))
			
			# Add the parsed details to our events list
			events.append(details)
		
		return events
	
	
	# "Private" methods
	
	@staticmethod
	def _expandRange(expr):
		'''
		Expands a range expression in the form "A-B", also handling single-item ranges in the form "A"
		'''
		if '-' not in expr:
			return [int(expr)]
		else:
			start, end = Timetable._splitAndVerify(expr, '-', 2)
			return list(range(int(start), int(end)+1))
	
	@staticmethod
	def _splitAndVerify(string, delim, expected):
		'''
		Splits a string and raises an error if the result is not of the expected length
		'''
		result = string.split(delim)
		if len(result) != expected:
			raise MalformedResultError
		return result
