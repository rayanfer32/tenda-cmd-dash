import logging
from views import showAdvancedStats
from utils import pauseScreen

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def main():
	# showSimpleStats()
	try:
		while True:
			showAdvancedStats()
	except Exception as e:
		print(e)
		logging.info(e)
		pauseScreen()

if __name__ == "__main__":
	main()

	
		