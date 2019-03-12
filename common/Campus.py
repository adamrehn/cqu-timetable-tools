# The IANA timezone identifiers for each Australian state
TIMEZONES = {
	'NSW': 'Australia/Sydney',
	'NT': 'Australia/Darwin',
	'QLD': 'Australia/Brisbane',
	'SA': 'Australia/Adelaide',
	'TAS': 'Australia/Hobart',
	'VIC': 'Australia/Melbourne',
	'WA': 'Australia/Perth'
}

class Campus(object):
	'''
	Provides functionality related to CQU campus locations
	'''
	
	@staticmethod
	def get_timezone(campus):
		'''
		Returns the IANA timezone identifier for the specified campus
		'''
		return {
			
			# Adelaide Campus
			'ADL': TIMEZONES['SA'],
			
			# Biloela Study Centre
			'BIL': TIMEZONES['QLD'],
			
			# Brisbane Campus
			'BNE': TIMEZONES['QLD'],
			
			# Bundaberg Campus
			'BDG': TIMEZONES['QLD'],
			
			# Cairns Campus
			'CNS': TIMEZONES['QLD'],
			
			# Cairns Study Hub
			'CSH': TIMEZONES['QLD'],
			
			# Emerald Campus
			'EMD': TIMEZONES['QLD'],
			
			# Gladstone, City Campus
			'GLC': TIMEZONES['QLD'],
			
			# Gladstone, Marina Campus
			'GLD': TIMEZONES['QLD'],
			
			# Mackay, City Campus
			'MKC': TIMEZONES['QLD'],
			
			# Mackay, Ooralea Campus
			'MKY': TIMEZONES['QLD'],
			
			# Melbourne Campus
			'MEL': TIMEZONES['VIC'],
			
			# Noosa Campus
			'NSA': TIMEZONES['QLD'],
			
			# Perth Campus
			'PER': TIMEZONES['WA'],
			
			# Rockhampton, City Campus
			'ROC': TIMEZONES['QLD'],
			
			# Rockhampton, North Campus
			'ROK': TIMEZONES['QLD'],
			
			# Sydney Campus
			'SYD': TIMEZONES['NSW'],
			
			# Townsville Campus
			'TVL': TIMEZONES['QLD'],
			
			# Townsville Study Hub
			'TNS': TIMEZONES['QLD'],
			
			# Yeppoon Study Centre
			'YPN': TIMEZONES['QLD']
			
		}.get(campus.upper(), None)
