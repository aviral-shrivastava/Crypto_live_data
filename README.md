# **Crypto Live Data Tracker**  

This project fetches live cryptocurrency data for the top 50 cryptocurrencies by market capitalization using a public API CoinGecko and performs basic analysis. The data is continuously updated in an Excel sheet every 5 minutes, providing real-time insights into market trends.  

## **Features**  
✅ Fetches real-time data for the top 50 cryptocurrencies  
✅ Extracts key metrics:  
- Cryptocurrency Name  
- Symbol  
- Current Price (in USD)  
- Market Capitalization  
- 24-hour Trading Volume  
- Price Change (24-hour %)  
✅ Performs basic analysis:  
- Identifies the **top 5** cryptocurrencies by market cap  
- Calculates the **average price** of the top 50 cryptocurrencies  
- Analyzes **highest & lowest** 24-hour percentage price change  
✅ Updates an **Excel sheet live** every 5 minutes  

## **Installation & Setup**  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/aviral-shrivastava/Crypto_live_data.git
   cd Crypto_live_data
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**  
   ```bash
   python crypto_tracker.py
   ```

## **Live Updating Excel Sheet**  
- The data is continuously updated in an Excel file (`crypto_data.xlsx`).  
- You can open the file while the script is running to see real-time updates.  

## **Project Structure**  
```
Crypto_live_data/
│── crypto_tracker.py  # Main script to fetch and analyze data
│── requirements.txt   # Required Python packages
│── crypto_data.xlsx   # Live updating Excel file
│── analysis_report.pdf # Key insights and findings
│── README.md          # Project documentation
```

## **Analysis Report**  
The **analysis report (analysis_report.pdf)** includes:  
- Market insights on top cryptocurrencies  
- Average price of top 50 cryptos  
- Most volatile cryptocurrencies in the last 24 hours  
- Observations on price trends  

## **Contributions & Issues**  
Feel free to **fork this repository** and submit **pull requests**.

📧 **Contact:** aviralshrivastava604@gmail.com  


