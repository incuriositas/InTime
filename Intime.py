import IntimeLib as il
import pandas as pd

df_181001 = il.mask_with_in1d(il.df_from_cju, "날짜", 20181001)

for i in range(len(df_181001)):
    if len(df_181001["계획"][i]) == 4:
        hour = int(df_181001["계획"][i][0:1])
    else:
        hour = int(df_181001["계획"][i][0:2])

    # print(hour)

cols = ['항공사', '현황']
new_df = il.one_hot(il.df_from_cju, cols)
print(il.df_from_cju.head(10))

