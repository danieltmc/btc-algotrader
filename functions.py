import pandas
import pickle
import requests

# Base URLs
api = "https://api.pro.coinbase.com"
sandbox_api = "https://api-public.sandbox.pro.coinbase.com"
# URL extensions
btc_usd = "/products/btc-usd"

# Create empty DataFrame
def create_df():
	return(pandas.DataFrame(columns=["Time","Price"]))

# Import existing historical data
def load_data():
	dataframe = pandas.read_pickle("historical.pkl")
	print("Pandas DataFrame imported")
	return(dataframe)

# Save historical data
def save_data(dataframe):
	dataframe.to_pickle("historical.pkl")
	print("Pandas DataFrame saved")
	return

# Fetch all open orders
def book_price():
	request = requests.get(api + btc_usd + "/book")
	json = request.json()
	# Only look at asking (selling) prices. Other contents of the dict are "sequence" (order #) and "bids" (buying prices)
	asking = json["asks"]
	total_weight = float(0)
	# Sum the total order volume of open sales
	for i in range(len(asking)):
		total_weight += float(list[i][1])
	avg_price = float(0)
	# Sum the total prices, accounting for the percentage of all open sales
	for i in range(len(asking)):
		relative_weight = float(list[i][1]) / total_weight
		ask_price = float(list[i][0])
		avg_price += ask_price * relative_weight
	# Calculate the weighted average of all open sales
	avg_price = avg_price / total_weight

# Request latest order (warning: can be small trade volume)
def last_price():
	request = requests.get(api + btc_usd + "/ticker")
	json = request.json()
	# Time is in SQL timestamp format
	time = json["time"][0:10] + " " + json["time"][11:19]
	# Store price as a float instead of a truncated string
	# price = f'{float(data["price"]):.2f}'
	price = float(json["price"])
	# Pass results as a tuple so time and price can be stored as a pair
	return(time, price)
