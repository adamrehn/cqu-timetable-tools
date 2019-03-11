import arrow, json, re, requests

class KeyDates(object):
	'''
	Provides functionality for parsing CQU Key Dates data
	'''
	
	@staticmethod
	def get_terms(year):
		'''
		Retrieves the list of weeks for all of the HE (Higher Education) terms in the specified year
		'''
		
		# Retrieve the list of key dates for HE
		dates = json.loads(
			re.search(
				'var heDates = ([^\n]+);\n',
				requests.get('https://handbook.cqu.edu.au/facet/key-dates/index').text
			).group(1)
		)
		
		# Extract the dates for the specified year and the next one (so we get all of T3 for the specified year)
		dates = [d for d in dates if arrow.get(d['start']).date().year in [year, year+1]]
		
		# Extract the start date for each week in each term
		weekRegex = re.compile('Week ([0-9]+) \\(Uni\\)', re.IGNORECASE)
		termWeeks = [d for d in dates if weekRegex.search(d['title']) is not None]
		termWeeks = sorted(termWeeks, key=lambda d: arrow.get(d['start']))
		
		# Group the weeks by term, ignoring the tail end of T3 from the previous year
		terms = []
		for week in termWeeks:
			
			# Extract the week number
			number = int(weekRegex.search(week['title']).group(1))
			
			# If this is Week 1, start a new term
			if number == 1:
				terms.append([])
			
			# Append the week to the current term
			if len(terms) > 0:
				terms[-1].append(week)
		
		return terms
