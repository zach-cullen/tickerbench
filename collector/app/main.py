from flask import Flask, jsonify
from concurrent.futures import ThreadPoolExecutor
import app.fetcher.stock_fetcher as fetcher


app = Flask(__name__)

# Create a thread pool with a maximum number of worker threads
MAX_WORKERS = 5  # Adjust this number based on your use case and server resources
executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

# Function simulating the data collector
def run_collector():
    print("Collector started.")
    fetcher.get_apple()
    print("Collector finished.")

# Function to submit the collector to the thread pool
def start_collector_task():
    print("Starting collector task.")
    executor.submit(run_collector)

# Endpoint to manually trigger the collector
@app.route('/run_collector', methods=['POST'])
def trigger_collector():
    start_collector_task()
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
