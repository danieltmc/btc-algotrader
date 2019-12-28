import pandas
import pickle
import requests

api = "https://api.pro.coinbase.com"
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

def get_price():
	request = requests.get(api+"/products/btc-usd/ticker")
	data = request.json()
	time = data["time"][0:10] + " " + data["time"][11:19]
	price = f'{float(data["price"]):.2f}'

	# Format is timestamp, numeric(7,2)
	# ('YYYY-MM-DD HH:MM:SS', xxxxx.yy)
