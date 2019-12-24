import pandas
import requests
# Import function definitions
import functions

# On start
try:
	global data
	data = load_data()

except IOError:
	global data
	data = pandas.DataFrame(columns=["Time","Price"])
