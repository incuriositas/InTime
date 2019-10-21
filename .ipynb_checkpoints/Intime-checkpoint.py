import IntimeLib as il

df_181001 = il.mask_with_in1d(il.df_from_cju, "날짜", 20181001)

for i in range(len(df_181001)):
    if len(df_181001["계획"][i]) == 4:
        hour = int(df_181001["계획"][i][0:1])
    else:
        hour = int(df_181001["계획"][i][0:2])

    print(hour)

print(il.df_to_gmp.head(5))
print(il.weather_cju_01.head(5))
