import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
df_tesla = pd.read_csv("data/TESLA Search Trend vs Price.csv")
df_unemployment = pd.read_csv("data/UE Benefits Search vs UE Rate 2004-19.csv")
df_btc_price = pd.read_csv("data/Daily Bitcoin Price.csv")
df_btc_search = pd.read_csv("data/Bitcoin Search Trend.csv")
print(df_tesla.shape)
print(df_tesla.head())
print(df_unemployment.shape)
print(df_unemployment.head())
print(df_tesla.columns)
print(df_unemployment.columns)
print(f"Largest for Eslata in Web Search: {df_tesla["TSLA_WEB_SEARCH"].max()}")
print(f"Smallest value for Tesla in Web Search: {df_tesla["TSLA_WEB_SEARCH"].min()}")
print(df_tesla.describe()) # Get summary statistics for Tesla dataframe
print(df_btc_price.shape) # Print shape of Bitcoin price dataframe
print(df_btc_price.head()) # Print first few rows of Bitcoin price dataframe
print(df_btc_search.shape) # Print shape of Bitcoin search trend dataframe
print(df_btc_search.head()) # Print first few rows of Bitcoin search trend dataframe
print(f"Largest BTC News Search value {df_btc_search["BTC_NEWS_SEARCH"].max()}") # Largest BTC News Search value
print(df_tesla.isna().values.any()) # Check for missing values in Tesla dataframe
print(df_unemployment.isna().values.any()) # Check for missing values in Unemployment dataframe
# print(df_btc_price.isna().values.any()) # Check for missing values in Bitcoin price dataframe
print(df_btc_search.isna().values.any()) # Check for missing values in Bitcoin search trend dataframe
df_btc_price = df_btc_price.dropna() # Remove rows with missing values in Bitcoin price dataframe
print(df_btc_price.isna().values.any()) # Verify no missing values remain in Bitcoin price dataframe
#Convert columns date where are strings to datetime objects
print(type(df_tesla["MONTH"][0])) # Check type of first entry in Tesla MONTH column
df_tesla["MONTH"] = pd.to_datetime(df_tesla["MONTH"]) # Convert Tesla MONTH column to datetime
print(type(df_tesla["MONTH"][0])) # Verify conversion to datetime
print(type(df_unemployment["MONTH"][0])) # Check type of first entry in Unemployment
df_unemployment["MONTH"] = pd.to_datetime(df_unemployment["MONTH"]) # Convert Unemployment MONTH column to datetime
print(type(df_unemployment["MONTH"][0])) # Verify conversion to datetime
print(type(df_btc_price["DATE"][0])) # Check type of first entry in Bitcoin price DATE column
df_btc_price["DATE"] = pd.to_datetime(df_btc_price["DATE"]) # Convert Bitcoin price DATE column to datetime
print(type(df_btc_price["DATE"][0])) # Verify conversion to datetime
print(type(df_btc_search["MONTH"][0])) # Check type of first entry in Bitcoin search trend DATE column
df_btc_search["MONTH"] = pd.to_datetime(df_btc_search["MONTH"]) # Convert Bitcoin search trend DATE column to datetime
print(type(df_btc_search["MONTH"][0])) # Verify conversion to datetime
#Resempling Time Series Data
df_btc_monthly = df_btc_price.resample("ME", on="DATE").last() # Resample Bitcoin price data to monthly frequency, taking last entry of each month
print(df_btc_monthly.shape) # Print shape of resampled Bitcoin monthly dataframe
print(df_btc_monthly.head()) # Print first few rows of resampled Bitcoin monthly dataframe
#Data Visualization - Tesla Line Charts
plt.figure(figsize=(14,8)) # Set figure size
ax1 = plt.gca() # Get current axes
ax2 = ax1.twinx() # Create a second y-axis sharing the same x-axis
ax1.plot(df_tesla["MONTH"], df_tesla["TSLA_USD_CLOSE"], color="c", linewidth= 3) # Plot Tesla web search data on primary y-axis
ax2.plot(df_tesla["MONTH"], df_tesla["TSLA_WEB_SEARCH"], color="red", linewidth= 3) # Plot Tesla price data on secondary y-axis
ax1.set_xlabel("Year", fontsize=14, rotation=45) # Set x-axis label
ax1.set_ylabel("TSLA Stock Price", fontsize=14, color="red") # Set y-axis label
ax2.set_ylabel("Search Trend", fontsize=14, color="c") #Set y-axis label for search trend
# Set the minimum and maximum values on the axes
ax1.set_ylim([0, 600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])
plt.title("Tesla Web Search vs Price", fontsize = 14) # Set plot title
#Using Locators and DateFormatters to generate Tick Marks on a Time Line
# Create locators for ticks on the time axis
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month 
years_fmt = mdates.DateFormatter('%Y')
# Format the ticks on the x-axis
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
plt.show() # Display the plot

#Data Visualization - BTC Line Charts
plt.figure(figsize=(14,8), dpi=120)
 
plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
plt.xticks(fontsize=14, rotation=45)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_ylabel('BTC Price', color='#F08F2E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
 
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
ax1.set_ylim(bottom=0, top=15000)
ax1.set_xlim([df_unemployment.index.min(), df_unemployment.index.max()])
# Experiment with the linestyle and markers
ax1.plot(df_unemployment.index, df_unemployment.UNRATE, 
         color='#F08F2E', linewidth=3, linestyle='--')
ax1.grid(color='grey', linestyle='--')
ax2.plot(df_unemployment.index, df_unemployment.UE_BENEFITS_WEB_SEARCH, 
         color='skyblue', linewidth=3, marker='o')
plt.show()

# Data Visualisation - Unemployment: How to use Grids
plt.figure(figsize=(14,8), dpi=120)
plt.title('Rolling Monthly US "Unemployment Benefits" Web Searches vs UNRATE', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
 
ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)
 
ax1.set_ylim(bottom=3, top=10.5)
ax1.set_xlim([df_unemployment.MONTH[0], df_unemployment.MONTH.max()])
 
# Calculate the rolling average over a 6 month window
roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
 
ax1.plot(df_unemployment.MONTH, roll_df.UNRATE, 'purple', linewidth=3, linestyle='-.')
ax2.plot(df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)
 
plt.show()