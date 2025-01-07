import yfinance as yf

def fetch_stock_data(ticker: str, start_date: str, end_date: str):
    """
    Fetch historical stock data from Yahoo Finance.

    Parameters:
        ticker (str): The stock ticker symbol (e.g., 'AAPL' for Apple).
        start_date (str): The start date for the historical data in 'YYYY-MM-DD' format.
        end_date (str): The end date for the historical data in 'YYYY-MM-DD' format.

    Returns:
        pandas.DataFrame: A DataFrame containing the historical stock data.
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date)
        print(f"Data for {ticker} from {start_date} to {end_date}:")
        print(data.head())
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_apple():
  ticker = "AAPL"
  start_date = "2024-01-01"
  end_date = "2024-12-31"

  print(f"Getting data for {ticker}")

  # Fetch stock data
  data = fetch_stock_data(ticker, start_date, end_date)
  
  # save data
  save_data_to_csv(data)

def save_data_to_csv(data):
  if data is not None:
      # Save the data to a CSV file
      output_file = f"test_data.csv"
      data.to_csv(output_file)
      print(f"Historical data saved to {output_file}")
