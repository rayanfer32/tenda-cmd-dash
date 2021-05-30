import logging
from views import showAdvancedStats
from utils import pauseScreen

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

def main():
	# showSimpleStats()
	try:
		while True:
			showAdvancedStats()
	except Exception as e:
		print(e)
		pauseScreen()

if __name__ == "__main__":
	main()

	
		