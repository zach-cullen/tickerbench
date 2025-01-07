import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from app.fetcher.stock_fetcher import fetch_stock_data

class TestFetchStockData(unittest.TestCase):

    @patch("app.fetcher.stock_fetcher.yf.Ticker")
    def test_fetch_stock_data_success(self, mock_ticker):
        # Mocking the DataFrame to return
        mock_data = pd.DataFrame({
            "Open": [100, 102, 101],
            "Close": [102, 103, 104],
            "High": [103, 104, 105],
            "Low": [99, 101, 100],
        }, index=pd.date_range("2023-01-01", "2023-01-03"))
        
        # Mock the Ticker object and its history method
        mock_ticker_instance = MagicMock()
        mock_ticker_instance.history.return_value = mock_data
        mock_ticker.return_value = mock_ticker_instance

        # Call the method
        result = fetch_stock_data("AAPL", "2023-01-01", "2023-01-03")

        # Assertions
        self.assertIsInstance(result, pd.DataFrame)
        pd.testing.assert_frame_equal(result, mock_data)

    @patch("app.fetcher.stock_fetcher.yf.Ticker")
    def test_fetch_stock_data_invalid_ticker(self, mock_ticker):
        # Simulate an empty DataFrame for an invalid ticker
        mock_ticker_instance = MagicMock()
        mock_ticker_instance.history.return_value = pd.DataFrame()
        mock_ticker.return_value = mock_ticker_instance

        # Call the method with an invalid ticker
        result = fetch_stock_data("INVALID", "2023-01-01", "2023-01-03")

        # Assertions
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(result.empty)

    @patch("app.fetcher.stock_fetcher.yf.Ticker")
    def test_fetch_stock_data_api_error(self, mock_ticker):
        # Simulate an exception
        mock_ticker.side_effect = Exception("API error")

        # Call the method
        result = fetch_stock_data("AAPL", "2023-01-01", "2023-01-03")

        # Assertions
        self.assertIsNone(result)

    @patch("app.fetcher.stock_fetcher.yf.Ticker")
    def test_fetch_stock_data_invalid_date_format(self, mock_ticker):
        # Simulate a ValueError for invalid date format
        mock_ticker_instance = MagicMock()
        mock_ticker_instance.history.side_effect = ValueError("Invalid date format")
        mock_ticker.return_value = mock_ticker_instance

        # Call the method
        result = fetch_stock_data("AAPL", "01-01-2023", "03-01-2023")

        # Assertions
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
