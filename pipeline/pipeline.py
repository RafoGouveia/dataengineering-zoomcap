import sys
import pandas as pd

print("arguments", sys.argv)

month = int(sys.argv[1])



df = pd.DataFrame({"day": [1, 2], "#Passengers": [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f"output_day_{month}.parquet")

print(f"Running pipeline for month {month}")

#https://youtu.be/lP8xXebHmuE?t=4314