import pandas
import requests
# Import function definitions
import functions

# Pandas DataFrame object
global data

try:
	# On start
	try:
		# Load Pickled DataFrame
		data = functions.load_data()	
	except IOError:
		# Create DataFrame if one does not already exist
		data = functions.create_df()
	
	
	
# On exit
except:
	print("Saving data before exit...")
	save_data(data)
	exit()
