from .Campus import Campus
from .KeyDates import KeyDates
from .Timetable import Timetable
import arrow, icalendar

# The days of the week, in the order recognised by Arrow for numeric indices
WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

class CalendarExport(object):
	'''
	Provides functionality for generating calendar data from timetable events
	'''
	
	@staticmethod
	def generate_calendar(filename, campus, term, subjects):
		'''
		Generates an iCalendar (RFC 5545) file for the timetable events for the specified subjects
		'''
		
		# Retrieve the dates for each of the weeks in the specified term
		currentYear = arrow.now().date().year
		termWeeks = KeyDates.get_terms(currentYear)[term-1]
		
		# Retrieve the timetable events for the specified subjects
		events = Timetable.get_events(campus, term, subjects)
		
		# Create a calendar to hold our generated calendar events
		calendar = icalendar.Calendar()
		calendar.add('prodid', '-//Adam Rehn//CQU Timetable Tools//EN')
		calendar.add('version', '2.0')
		
		# Iterate over the timetable events and generate corresponding calendar events
		total = 0
		for event in events:
			
			# Generate a calendar event for each week
			for week in event['weeks']:
				
				# Determine the numeric index of the weekday for the event
				dayNum = WEEKDAYS.index(event['day'].capitalize())
				
				# Parse the start time and end time for the event and determine the duration
				startTime = arrow.get(event['start'], 'HH:mm')
				endTime = arrow.get(event['end'], 'HH:mm')
				duration = endTime - startTime
				
				# Compute the start date/time for the event
				start = arrow.get(termWeeks[week-1]['start'])
				start = start.shift(weekday=dayNum, hours=startTime.time().hour, minutes=startTime.time().minute)
				
				# Convert the start date/time from the local campus timezone to UTC
				campusTimezone = Campus.get_timezone(campus)
				start.tzinfo = arrow.parser.TzinfoParser.parse(campusTimezone)
				start = start.to('UTC')
				
				# Compute the end date/time for the event
				end = start.shift(seconds=duration.seconds)
				
				# Create the event and add it to the calendar
				calEvent = icalendar.Event()
				calEvent.add('summary', '{} {} (Week {})'.format(event['code'].upper(), event['type'].capitalize(), week))
				calEvent.add('description', '{} {}'.format(event['code'], event['name']))
				calEvent.add('location', event['location'])
				calEvent.add('dtstart', start.datetime)
				calEvent.add('dtend', end.datetime)
				calEvent.add('dtstamp', arrow.utcnow().datetime)
				calendar.add_component(calEvent)
				
				# Keep track of the total number of generated events
				total += 1
		
		# Write the generated calendar events to file
		with open(filename, 'wb') as f:
			f.write(calendar.to_ical())
		
		# Return the number of generated events
		return total
