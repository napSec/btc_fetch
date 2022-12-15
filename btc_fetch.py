# Import the necessary libraries
import requests
import json

# Define a function to fetch the transactions for a given address
def fetch_transactions(address, start_date, end_date):
  # Construct the URL for the request
  url =f'https://blockchain.info/rawaddr/{address}?start={start_date}&end={end_date}'
  
  # Send the request and parse the response
  response = requests.get(url)
  data = response.json()
  
  # Return the list of transactions
  return data['txs']

# Prompt the user for the address and date range to search
address = input('Enter the Bitcoin address: ')
start_date = input('Enter the start date (YYYY-MM-DD): ')
end_date = input('Enter the end date (YYYY-MM-DD): ')

# Fetch the transactions for the specified address and date range
transactions = fetch_transactions(address, start_date, end_date)

# Print the transactions
print(json.dumps(transactions, indent=2))


