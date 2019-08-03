import pg8000
from config import *

connect = pg8000.connect(user=username, password=password)
cursor = connect.cursor()

cursor.execute("SHOW TABLES LIKE 'btc_prices'")
