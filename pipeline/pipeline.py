import datetime
today=datetime.datetime.today()
print("Snapshot datetime : ", today)

import pandas as pd
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())

df.to_parquet(f"output_day_{today.date()}.parquet")