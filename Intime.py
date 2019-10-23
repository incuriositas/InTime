import IntimeLib as il
import pandas as pd
import FlieLib as fl

"""
# 항공기 csv (in FileLib)
flight_from_cju / flight_from_gmp
flight_to_cju / flight_to_gmp
(DataFrame)

# 날씨 csv (in FileLib)
weather_cju / weather_gmp
(List of DataFrame)
"""

new_df_ = il.month_slice(fl.flight_from_cju, 20181101, 30)

cols = ['현황','항공사']
new_df = il.one_hot(new_df_, cols)
merged_df = pd.merge(new_df, fl.weather_cju[1], on="TM")
new_merge = merged_df.dropna(axis=1)
new_merge.drop(["날짜", "Time", "Date", "time"],
               axis=1, inplace=True)
# print(new_merge.head())
il.display_heatmap(new_merge)
