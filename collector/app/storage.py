def save_data_to_csv(ticker, data):
  if data is not None:
      # Save the data to a CSV file
      output_file = f"app/output/{ticker}_test_data.csv"
      data.to_csv(output_file)
      print(f"Historical data saved to {output_file}")