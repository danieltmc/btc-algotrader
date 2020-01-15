import pandas
import pickle
import requests
import time

# Base URLs
api = "https://api.pro.coinbase.com"
sandbox_api = "https://api-public.sandbox.pro.coinbase.com"
websocket = "wss://ws-feed.pro.coinbase.com"
sandbox_websocket = "wss://ws-feed-public.sandbox.pro.coinbase.com"
# URL extensions
btc_usd = "/products/btc-usd"

###############################
# Data Storage Functions
###############################

# Create empty DataFrame
def create_df():
	# Time is the index of the DataFrame, Price and Volume are the data to be stored
	main.data = pandas.DataFrame(columns = ["Time", "Price", "Volume"])
	return

# Import existing historical data
def load_data():
	main.data = pandas.read_pickle("historical.pkl")
	print("Pandas DataFrame imported")
	return

# Save historical data
def save_data():
	main.data.to_pickle("historical.pkl")
	print("Pandas DataFrame saved")
	return

# Write current price to the DataFrame
def log_price():
	# Use weighted average and volume of top 50 open sales
	time, price, volume = book_price()
	# Add row at end of DataFrame, divide size of DataFrame by number of columns to get the index of the next row
	main.data = main.data.append({"Time": time, "Price": price, "Volume": volume}, ignore_index = True)
	print("Data logged: Average price of $" + str(price) + "across total order volume of " + str(volume) " BTC")
	return

###############################
# Order Data Functions
###############################

# Fetch open orders
def book_price():
	# Make requests first to minimize delay between time and price
	time_request = requests.get(api + btc_usd + "/time")
	order_request = requests.get(api + btc_usd + "/book?level=2") # Level 2 gives top 50 open orders
	# Time is in SQL timestamp format
	time_json = time_request.json()
	time = format_time(time_json["iso"])
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
	return(time, weighted_price, total_weight)

# Request latest order (warning: can be small trade volume)
def last_price():
	request = requests.get(api + btc_usd + "/ticker")
	json = request.json()
	# Time is in SQL timestamp format
	time = format_time(json["time"])
	# Store price as a float instead of a truncated string
	# price = f'{float(data["price"]):.2f}'
	price = float(json["price"])
	# Pass results as a tuple so time and price can be stored as a pair
	return(time, price)

###############################
# Data Manipulation Functions
###############################

def hour_avg(dataframe):
	main.data.loc[main.data["Time"] > relative_timestamp(hours=1)]

###############################
# Utility Functions
###############################

# Convert time from ISO to SQL timestamp
def format_time(unformatted):
	formatted = unformatted[0:10] + " " + unformatted[11:19]
	return(formatted)

# Return time in SQL timestamp format
def timestamp():
	return(time.strftime("%Y-%m-%d %H:%M:%S"))

# Return past time in SQL timestamp format
def relative_timestamp(weeks = 0, days = 0, hours = 0, minutes = 0, seconds = 0):
	timestamp = int(time.time()) - ((minutes * 60) + (hours * 3600) + (days * 86400) + (weeks * 604800))
	return(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(timestamp)))
