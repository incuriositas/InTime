import IntimeLib as il
import pandas as pd
import FlieLib as fl

"""
# 항공기 csv (in FileLib)
flight_from_cju : 제주에서 출발하여 김포로 도착 (출발한 당시) -> 제주공항날씨
flight_from_gmp  : 김포에서 출발하여 제주로 도착 (출발한 당시) -> 김포공항날씨
flight_to_cju  : 김포에서 출발하여 제주로 도착 (도착한 당시) -> 제주공항날씨
flight_to_gmp  : 제주에서 출발하여 김포로 도착 (도착한 당시) -> 김포공항날씨
(DataFrame)

# 날씨 csv (in FileLib)
weather_cju / weather_gmp
(List of DataFrame)
"""

new_df_ = il.month_slice(fl.flight_from_cju, 20181101, 30)


cols = ['현황']
new_df = il.one_hot(new_df_, cols)
merged_df = pd.merge(new_df, fl.weather_cju[1], on="TM")
new_merge = merged_df.dropna(axis=1)

new_merge.drop(["날짜", "Time", "Date", "time"],
               axis=1, inplace=True)
# il.display_heatmap(new_merge)
print(new_df.info())
print(new_merge.info())
