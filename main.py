import os
import logging
import json
import api
from views import showAdvancedStats

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

def main():
	while True:
		# showSimpleStats()
		showAdvancedStats()

if __name__ == "__main__":
	main()
	# api.getAllStatsJson()
	
	# # save allStats to a file
	# with open("getAllStats.json", 'w') as f:
	# 	json.dump(api.getAllStatsJson(), f)
	
		