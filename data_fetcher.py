import ccxt
import pandas as pd

# Initialize Uniswap V3 (Ethereum)
exchange = ccxt.uniswap_v3({
    'enableRateLimit': True,
})

# WEPE/USDT trading pair (adjust if paired with ETH or another token)
symbol = 'WEPE/USDT'  # Check Uniswap for exact pair (e.g., WEPE/ETH)
timeframe = '1h'      # 1-hour candles
limit = 1000          # Number of data points

try:
    # Fetch historical data
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    
    # Convert to DataFrame
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Save to CSV
    df.to_csv('wepe_data.csv', index=False)
    print("Data fetched and saved to wepe_data.csv")
except ccxt.NetworkError as e:
    print(f"Network error: {e}")
except ccxt.ExchangeError as e:
    print(f"Exchange error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")