# ==============================================================================
# Project: Coca Cola Stock - Live and Updated
#
# Objective:
# To perform a comprehensive data analysis on The Coca-Cola Company's historical
# stock data. The analysis will focus on visualizing price trends, trading volume,
# and key technical indicators to gain insights into the stock's performance over time.
#
# Datasets:
# - Coca-Cola_stock_history.csv: Contains daily historical stock prices and volume.
# - Coca-Cola_stock_info.csv: Contains general company and stock information.
# ==============================================================================

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set a professional plotting style for better visualization
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('viridis')

# 2. Data Loading and Initial Exploration
# ------------------------------------------------------------------------------
try:
    stock_history_df = pd.read_csv('Coca-Cola_stock_history.csv')
    stock_info_df = pd.read_csv('Coca-Cola_stock_info.csv')
except FileNotFoundError:
    print("Error: One or more CSV files were not found.")
    print("Please ensure 'Coca-Cola_stock_history.csv' and 'Coca-Cola_stock_info.csv' are in the same directory as the script.")
    exit()

print("--- Historical Stock Data Info ---")
print("Shape of the dataset (rows, columns):", stock_history_df.shape)
print("\nFirst 5 rows of the dataset:")
print(stock_history_df.head())
print("\nDataset information:")
stock_history_df.info()
print("\nMissing values in the dataset:")
print(stock_history_df.isnull().sum())

print("\n--- Company Information ---")
print(stock_info_df)

# 3. Data Cleaning and Preprocessing
# ------------------------------------------------------------------------------
# Convert the 'Date' column to a proper datetime object for time-series analysis.
# FIX: 1. Use format='mixed' and utc=True to handle mixed timezones and silence the FutureWarning.
# FIX: 2. Use .dt.tz_localize(None) to remove timezone information after conversion.
# This prevents the matplotlib UserWarning, as the exact time of day is irrelevant for daily stock data.
stock_history_df['Date'] = pd.to_datetime(stock_history_df['Date'], format='mixed', utc=True).dt.tz_localize(None)

# Set the 'Date' column as the index for easier time-series operations
stock_history_df.set_index('Date', inplace=True)

# Drop columns that provide no analytical value (e.g., if they contain only one unique value like 0)
columns_to_drop = ['Dividends', 'Stock Splits']
for col in columns_to_drop:
    if col in stock_history_df.columns and stock_history_df[col].nunique() <= 1:
        stock_history_df.drop(columns=[col], inplace=True)

# 4. Exploratory Data Analysis (EDA)
# ------------------------------------------------------------------------------

# --- 4.1: Visualize Historical Price and Volume ---
plt.figure(figsize=(16, 12))

# Plot the 'Close' price over time
plt.subplot(2, 1, 1)
plt.plot(stock_history_df.index, stock_history_df['Close'], label='Closing Price', color='dodgerblue')
plt.title('Coca-Cola Stock Closing Price History', fontsize=18)
plt.xlabel('')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)

# Plot the 'Volume' over time
plt.subplot(2, 1, 2)
plt.bar(stock_history_df.index, stock_history_df['Volume'], color='darkcyan')
plt.title('Coca-Cola Stock Trading Volume', fontsize=18)
plt.xlabel('Date')
plt.ylabel('Volume')
plt.grid(True)
plt.tight_layout()
plt.show()

# --- 4.2: Analyze Distribution of Prices ---
plt.figure(figsize=(14, 6))
sns.histplot(stock_history_df[['Open', 'High', 'Low', 'Close']], kde=True, bins=50, palette='Pastel1')
plt.title('Distribution of Stock Prices', fontsize=16)
plt.xlabel('Price ($)')
plt.ylabel('Frequency')
plt.legend(title='Price Type', labels=['Open', 'High', 'Low', 'Close'])
plt.show()

# --- 4.3: Calculate and Plot Moving Averages ---
# Calculate a 50-day and 200-day Simple Moving Average (SMA)
stock_history_df['SMA_50'] = stock_history_df['Close'].rolling(window=50).mean()
stock_history_df['SMA_200'] = stock_history_df['Close'].rolling(window=200).mean()

plt.figure(figsize=(16, 8))
plt.plot(stock_history_df.index, stock_history_df['Close'], label='Closing Price', color='dodgerblue')
plt.plot(stock_history_df.index, stock_history_df['SMA_50'], label='50-Day SMA', color='orange', linestyle='--')
plt.plot(stock_history_df.index, stock_history_df['SMA_200'], label='200-Day SMA', color='red', linestyle='--')
plt.title('Coca-Cola Stock Price with Moving Averages', fontsize=18)
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.show()

# 5. Summary of Findings
# ------------------------------------------------------------------------------
# Based on the exploratory data analysis, the following key observations can be made:
#
# - Long-Term Trend: The stock shows a clear long-term upward trend, with periods of
#   volatility and consolidation.
# - Moving Averages: The 50-day and 200-day moving averages provide a good
#   indication of the long-term trend. The price consistently stayed above the 200-day
#   SMA, which is generally considered a bullish signal.
# - Trading Volume: The trading volume shows significant spikes over the years,
#   indicating periods of high trading activity, possibly driven by major news or
#   market events.
# - Price Distribution: The distribution of Open, High, Low, and Close prices is
#   skewed, indicating periods of price growth and stability.
#
# These insights form the foundation for more advanced analysis, such as building
# a predictive model or a trading strategy.

