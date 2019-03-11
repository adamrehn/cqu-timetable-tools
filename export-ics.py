#!/usr/bin/env python3
from common import CalendarExport
import arrow, icalendar, sys

# Verify that the required command-line arguments are present
if len(sys.argv) > 4:
	
	# Progress output
	print('Exporting...', flush=True)
	
	# Perform the export
	count = CalendarExport.generate_calendar(
		sys.argv[1],
		sys.argv[2],
		int(sys.argv[3]),
		sys.argv[4:]
	)
	
	# Progress output
	print('Exported {} events.'.format(count), flush=True)
	
else:
	print('Usage:')
	print('{} OUTFILE.ICS CAMPUS TERM SUBJECT1 SUBJECT2 ... SUBJECTN'.format(sys.argv[0]))
	print()
	print('Example:')
	print('{} timetable.ics CNS 1 COIT11222 COIT13234'.format(sys.argv[0]))
	print()
	print('This will export the events for these two subjects for Term 1 on the Cairns campus.')
