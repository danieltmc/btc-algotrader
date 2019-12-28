import pandas
import requests
# Import function definitions
import functions

try:
	# On start
	try:
		global data
		# Load Pickled DataFrame
		data = load_data()	
	except IOError:
		global data
		# Create DataFrame if one does not already exist
		data = pandas.DataFrame(columns=["Time","Price"])
# On exit
except KeyboardInterrupt:
	print("Saving data before exit...")
	save_data(data)
	
