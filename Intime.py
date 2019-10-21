import IntimeLib as il
import pandas as pd

df_181001 = il.mask_with_in1d(il.df_from_cju, "날짜", 20181001)

for i in range(len(df_181001)):
    if len(df_181001["계획"][i]) == 4:
        hour = int(df_181001["계획"][i][0:1])
    else:
        hour = int(df_181001["계획"][i][0:2])

    # print(hour)

cols = ['현황']
new_df = il.one_hot(il.flight_from_cju, cols)
new_df_10 = il.mask_with_in1d(new_df, "날짜", 20181001)

merged_df = pd.merge(new_df_10, il.weather_cju_10, on="TM")
new_merge = merged_df.dropna(axis=1)
new_merge.drop(["날짜", "Time", "Date", "항공사"], axis=1, inplace=True)
print(new_merge.head())

il.display_heatmap(new_merge)
