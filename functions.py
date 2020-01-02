import pandas
import pickle
import requests

api = "https://api.pro.coinbase.com"
btc_usd = "/products/btc-usd"
sandbox_api = "https://api-public.sandbox.pro.coinbase.com"

def create_df():
	# Create empty DataFrame
	return(pandas.DataFrame(columns=["Time","Price"]))

def load_data():
	# Import existing historical data
	dataframe = pandas.read_pickle("historical.pkl")
	print("Pandas DataFrame imported")
	return(dataframe)

def save_data(dataframe):
	# Save historical data
	dataframe.to_pickle("historical.pkl")
	print("Pandas DataFrame saved")
	return

def book_price():
	# Fetch all open orders
	request = requests.get(api + btc_usd + "/book")
	json = request.json()
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

def last_price():
	# Request latest order (warning: can be a very small amount)
	request = requests.get(api + btc_usd + "/ticker")
	data = request.json()
	# Time is in SQL timestamp format
	time = data["time"][0:10] + " " + data["time"][11:19]
	# Price is truncated to 2 decimal places
	price = f'{float(data["price"]):.2f}'
