#!/usr/bin/env python3
from common import Subjects, Timetable
import json, sys

# Verify that the required command-line arguments are present
if len(sys.argv) > 4:
	
	# Expand any wildcards in the supplied subject list
	subjects = Subjects.get_subjects(sys.argv[4:])
	
	# Progress output
	print('Exporting event data for the following subjects:')
	for subject in subjects:
		print('- {}'.format(subject))
	print(flush=True)
	
	# Retrieve the event data from the timetable
	events = Timetable.get_events(
		sys.argv[2],
		int(sys.argv[3]),
		subjects
	)
	
	# Write the data to the output file
	with open(sys.argv[1], 'w') as outfile:
		outfile.write(json.dumps(events, indent=4))
	
	# Progress output
	print('Exported data for {} events.'.format(len(events)), flush=True)
	
else:
	print('Usage:')
	print('{} OUTFILE.JSON CAMPUS TERM SUBJECT1 SUBJECT2 ... SUBJECTN'.format(sys.argv[0]))
	print()
	print('Example:')
	print('{} timetable.JSON CNS 1 COIT11222 COIT13234'.format(sys.argv[0]))
	print()
	print('This will export the events for these two subjects for Term 1 on the Cairns campus.')
	print('Note that wildcards are also supported. For example, the pattern "COIT1*" will match')
	print('all first-year IT subjects.')
