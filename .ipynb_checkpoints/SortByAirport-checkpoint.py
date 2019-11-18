# -*- coding: utf-8 -*-

import pandas as pd
import ReorderCSV


def sort_and_rewrite(load, temp, save, col, sort_by, new_col):
    print(load + " is running")
    origin = pd.read_csv(load)
    new_df = origin[origin[col] == sort_by]
    new_df.drop('Unnamed: 0', axis=1, inplace=True)
    new_df.to_csv(temp, encoding='utf-8-sig', index=False)

    df = pd.read_csv(temp)
    test_df = pd.DataFrame(columns=new_col)
    for j in range(len(df)):
        temp_list = [df.loc[j][0]]
        for i in range(1, len(df.loc[j])):
            temp_list.append(df.loc[j][i][1:-1])
        test_df.loc[j] = temp_list

    test_df.to_csv(save, encoding='utf-8-sig')
    print(load + " is done")


from_CJU_save = 'dataset/SortedCSV/Flight_from_CJU(Sorted).csv'
from_CJU_temp = 'dataset/SortedCSV/Flight_from_CJU_temp.csv'
from_CJU_load = 'dataset/OrderedCSV/Flight_from_CJU.csv'

from_GMP_save = 'dataset/SortedCSV/Flight_from_GMP(Sorted).csv'
from_GMP_temp = 'dataset/SortedCSV/Flight_from_GMP_temp.csv'
from_GMP_load = 'dataset/OrderedCSV/Flight_From_GMP.csv'

to_CJU_save = 'dataset/SortedCSV/Flight_to_CJU(Sorted).csv'
to_CJU_temp = 'dataset/SortedCSV/Flight_to_CJU_temp.csv'
to_CJU_load = 'dataset/OrderedCSV/Flight_to_CJU.csv'

to_GMP_save = 'dataset/SortedCSV/Flight_to_GMP(Sorted).csv'
to_GMP_temp = 'dataset/SortedCSV/Flight_to_GMP_temp.csv'
to_GMP_load = 'dataset/OrderedCSV/Flight_to_GMP.csv'

# sort_and_rewrite(from_CJU_load, from_CJU_temp, from_CJU_save, '도착', "'GMP(김포)'", ReorderCSV.to_col)
# sort_and_rewrite(to_CJU_load, to_CJU_temp, to_CJU_save, '출발지', "'GMP(김포)'", ReorderCSV.to_col)
# sort_and_rewrite(from_GMP_load, from_GMP_temp, from_GMP_save, '도착', "'CJU(제주)'", ReorderCSV.from_col)
# sort_and_rewrite(to_GMP_load, to_GMP_temp, to_GMP_save, '출발지', "'CJU(제주)'", ReorderCSV.from_col)
