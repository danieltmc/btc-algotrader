import pg8000
import requests

api = "https://api.pro.coinbase.com"

try:
	connect = pg8000.connect(user="btc", password="Bitcoin")
	cursor = connect.cursor()

	time_request = requests.get(api+"/time")
	time_data = time_request.json()
	formatted_time = time_data["iso"][0:10] + " " + time_data["iso"][11:19]

	price_request = requests.get(api+"/products")
	price_data = price_request.json()
	i = 0
	while (price_data[i]["id"] != "BTC-USD"):
		i=i+1

	# Format is timestamp, numeric(7,2)
	# ('YYYY-MM-DD HH:MM:SS', xxxxx.yy)
	cursor.execute("INSERT INTO btc_price ()")

except pg8000.DatabaseError:
	

finally:
	
