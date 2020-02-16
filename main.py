import pg8000
import requests

api = "https://api.pro.coinbase.com"

def get_price():
	try:
		connect = pg8000.connect(user="btc", password="Bitcoin")
		cursor = connect.cursor()
	
		request = requests.get(api+"/products/btc-usd/ticker")
		data = request.json()
		time = data["time"][0:10] + " " + data["time"][11:19]
		price = f'{float(data["price"]):.2f}'
	
		# Format is timestamp, numeric(7,2)
		# ('YYYY-MM-DD HH:MM:SS', xxxxx.yy)
		# TODO: Fix SQL syntax
		#cursor.execute("INSERT INTO btc_price VALUES (\'" + time + "\', " + price + ");")
	
	except pg8000.DatabaseError:
		
	
	finally:
		

