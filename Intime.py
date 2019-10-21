import IntimeLib as il

df_181001 = il.mask_with_in1d(il.df_from_cju, "날짜", 20181001)

for i in range(len(il.df_gmp_10)):
    if int(il.df_gmp_10["TM"][i]/100) == 20181001:
        pass
    else:
        il.df_gmp_10.drop(i, axis=0, inplace=True)


col = il.one_hot(il.df_from_cju, "현황")
print(il.df_gmp_10)