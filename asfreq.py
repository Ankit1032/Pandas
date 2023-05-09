import pandas as pd

# Create a DataFrame with a datetime index
index = pd.date_range(start='2023-01-01', end='2023-01-14', freq='D')
data = {'Value': [10, 20, 30, 40, 50, 60, 70, 90, 23, 17, 100, 98, 45, 87]}
df = pd.DataFrame(data, index=index)

# Upsample the data to an hourly frequency
df_hourly = df.asfreq('H')

# Downsample the data to a weekly frequency
df_weekly = df.asfreq('W')

#print(df_hourly)
print(df_weekly)

"""
In Pandas, the asfreq() function is used to convert a time series to a specified frequency. 
It allows you to upsample or downsample your data, changing the frequency at which the data is reported.

The asfreq() function is typically used with a datetime index in a DataFrame or a Series. 
It takes a single parameter, freq, which specifies the desired frequency of the resulting data. 
The freq parameter can be a string representing a frequency code (e.g., 'D' for daily, 'H' for hourly) or a Pandas offset alias.

Notes :
In the above example, the original DataFrame df has a daily frequency. The asfreq('H') call converts the data 
to an hourly frequency by adding rows with missing data for the hours in between. The asfreq('W') call converts 
the data to a weekly frequency by aggregating the daily values.
"""
