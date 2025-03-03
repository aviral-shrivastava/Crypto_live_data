import requests
import json
import pandas as pd
import time


# Function to fetch top 50 cryptos
def fetch_top_50_cryptos():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",          # Prices in USD
        "order": "market_cap_desc",    # Sort by market cap (descending)
        "per_page": 50,                # Fetch top 50 cryptocurrencies
        "page": 1,                     # Page number
        "sparkline": False             # No sparkline data
    }

    # GET request
    response = requests.get(url, params=params)

    if response.status_code == 200:
        # Parsing JSON
        data = response.json()
        
        # Required parameters
        formatted_data = []
        for crypto in data:
            crypto_info = {
                "Cryptocurrency name": crypto['name'],
                "Symbol": crypto['symbol'],
                "Current Price (in USD)": crypto['current_price'],
                "Market Capitalization": crypto['market_cap'],
                "24-hour Trading Volume": crypto['total_volume'],
                "Price Change (24-hour, percentage)": crypto['price_change_percentage_24h']
            }
            formatted_data.append(crypto_info)
        
        return formatted_data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None


# Function to analyze the data    
def analyze_data(data):
    # Top 5 cryptocurrencies 
    sorted_by_market_cap = sorted(data, key=lambda x: x['Market Capitalization'], reverse=True)
    top_5_by_market_cap = sorted_by_market_cap[:5]

    # Average price of top 50 cryptocurrencies
    total_price = sum(crypto['Current Price (in USD)'] for crypto in data)
    average_price = total_price / len(data)

    # Highest and lowest 24-hour price change
    highest_change = max(data, key=lambda x: x['Price Change (24-hour, percentage)'])
    lowest_change = min(data, key=lambda x: x['Price Change (24-hour, percentage)'])

    return {
        "top_5_by_market_cap": top_5_by_market_cap,
        "average_price": average_price,
        "highest_change": highest_change,
        "lowest_change": lowest_change
    }


# Fetch and display the data
data = fetch_top_50_cryptos()
if data:
    for crypto in data:
        print(crypto)
else:
    print("No data fetched.")


# Perform analysis
analysis_results = analyze_data(data)

# Display results
print("\nTop 5 Cryptocurrencies by Market Cap:")
for crypto in analysis_results['top_5_by_market_cap']:
    print(f"{crypto['Cryptocurrency name']} ({crypto['Symbol']}): ${crypto['Market Capitalization']:,.2f}")

print(f"\nAverage Price of Top 50 Cryptocurrencies: ${analysis_results['average_price']:.2f}")

print("\nHighest 24-Hour Price Change:")
print(f"{analysis_results['highest_change']['Cryptocurrency name']} ({analysis_results['highest_change']['Symbol']}): {analysis_results['highest_change']['Price Change (24-hour, percentage)']:.2f}%")

print("\nLowest 24-Hour Price Change:")
print(f"{analysis_results['lowest_change']['Cryptocurrency name']} ({analysis_results['lowest_change']['Symbol']}): {analysis_results['lowest_change']['Price Change (24-hour, percentage)']:.2f}%")


# Save data to JSON file
if data:
    with open("crypto_data.json", "w") as file:
        json.dump(data, file, indent=4)
    print("\nData saved to crypto_data.json")


# Save analysis results to JSON file
with open("analysis_results.json", "w") as file:
    json.dump(analysis_results, file, indent=4)
print("Analysis results saved to analysis_results.json")


# Function to update Excel sheet
def update_excel(data):
    df = pd.DataFrame(data)
    
    df.to_excel("crypto_data.xlsx", index=False)
    print("Excel sheet updated.")


# Loop to fetch and update data after every 300 seconds (5 minutes)
while True:
    data = fetch_top_50_cryptos()
    if data:
        update_excel(data)
    else:
        print("No data fetched. Retrying in 5 minutes")
    
    # Wait for 300 seconds (5 minutes)
    time.sleep(300)