import pandas
import requests
# Import function definitions
import functions

try:
	# On start
	try:
		global data
		# Load Pickled DataFrame
		data = functions.load_data()	
	except IOError:
		global data
		# Create DataFrame if one does not already exist
		data = functions.create_df()
# On exit
except:
	print("Saving data before exit...")
	save_data(data)
	exit()
