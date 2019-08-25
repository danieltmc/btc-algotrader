import java.sql.*;
import java.net.*;
import java.io.*;

public class PriceFetcher
{
	String url = "jdbc:postgresql:btc";
	
	public double get_price()
	{
		try
		{
			URLConnection connection = new URL("https://api.pro.coinbase.com/products/btc-usd/ticker").openConnection();
			BufferedReader input = new BufferedReader(new InputStreamReader(connection.getInputStream()));
			return(0.0);
		}
		catch (Exception e)
		{
			e.printStackTrace();
			return(-1.0);
		}
	}
	
	public boolean table_insert()
	{
		// Format is timestamp, numeric(7,2)
		// ("YYYY-MM-DD HH:MM:SS", xxxxx.yy)
		try
		{
			Connection db = DriverManager.getConnection(url, "btc", "Bitcoin");
			return(true);
		}
		catch (Exception e)
		{
			e.printStackTrace();
			return(false);
		}
	}
	
	public static void main(String[] args)
	{
		PriceFetcher fetcher = new PriceFetcher();
		try
		{
			
		}
		catch (Exception e)
		{
			e.printStackTrace();
		}
	}
}
