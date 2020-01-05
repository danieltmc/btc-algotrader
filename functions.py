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
	# Make requests first to minimize delay between time and price
	time_request = requests.get(api + btc_usd + "/time")
	order_request = requests.get(api + btc_usd + "/book?level=2") # Level 2 gives top 50 open orders
	# Time is in SQL timestamp format
	time_json = time_request.json()
	time = time_json["iso"][0:10] + " " + time_json["time"][11:19]
	# Only look at asking (selling) prices. Other contents of the dict are "sequence" (order #) and "bids" (buying prices)
	order_json = order_request.json()
	asking = order_json["asks"]
	total_weight = float(0)
	# Sum the total order volume of open sales
	for i in range(len(asking)):
		total_weight += float(asking[i][1])
	weighted_price = float(0)
	# Sum the total prices, accounting for the percentage of all open sales
	for i in range(len(asking)):
		relative_weight = float(asking[i][1]) / total_weight
		ask_price = float(asking[i][0])
		weighted_price += ask_price * relative_weight
	# Calculate the weighted average of all open sales
	weighted_price = weighted_price / total_weight
	return(time, weighted_price)

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

