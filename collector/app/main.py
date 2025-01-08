from flask import Flask, jsonify
from concurrent.futures import ThreadPoolExecutor
import app.fetcher as fetcher
import app.storage as storage

app = Flask(__name__)

# Create a thread pool with a maximum number of worker threads
MAX_WORKERS = 5  # Adjust this number based on your use case and server resources
executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)
TICKERS = ["GOOGL", "AAPL", "AMZN", "META",  "MSFT", "NVDA", "TSLA"]

# fetch data for one ticker and save to storage
def collect_stock_data(ticker: str, start_date: str, end_date: str):
    data = fetcher.fetch_stock_data(ticker, start_date, end_date)
    storage.save_data_to_csv(ticker, data)
    print(f"Saved {ticker} data to csv")

# Simiulate running all collector tasks using thread pool
def run_collector():
    print("Collector started.")
    for ticker in TICKERS:
        executor.submit(collect_stock_data(ticker, "2024-01-01", "2024-12-31"))
    print("Collector finished.")

# Endpoint to manually trigger the collector
@app.route('/run_collector', methods=['POST'])
def trigger_collector():
    run_collector()
    return jsonify({"message": "Collector triggered"}), 200

# Health check or main endpoint
@app.route('/')
def index():
    return jsonify({"message": "Flask app is running!"})

if __name__ == '__main__':
    # Start the collector immediately when the app initializes
    print("STARTED FLASK APP")
    # start_collector_task()
    app.run(host='0.0.0.0', port=5000)
