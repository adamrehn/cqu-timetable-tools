import itertools, re, requests

class Subjects(object):
	'''
	Provides functionality for querying CQU unit codes
	'''
	
	@staticmethod
	def get_subjects(codes):
		'''
		Retrieves the list of subjects matching the specified unit code search strings
		'''
		return list(itertools.chain.from_iterable([
			Subjects._query(code) for code in codes
		]))
	
	
	# "Private" methods
	
	@staticmethod
	def _query(code):
		'''
		Queries the CQU subject database to find subjects matching the specified unit code search string
		'''
		if '*' not in code:
			return [code]
		else:
			prefix = code[0 : code.index('*')]
			regex = re.compile(code.replace('*', '.*'), re.IGNORECASE)
			matches = requests.get('https://handbook.cqu.edu.au/facet/timetables/searchUnits', params = {
				'searchTxt': prefix
			}).json()
			return list([m['coursecode'] for m in matches if regex.fullmatch(m['coursecode']) is not None])
