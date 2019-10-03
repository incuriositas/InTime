# -*- coding: utf-8 -*-

import pandas as pd

to_col = ['날짜', '항공사', '편명', '출발지', '계획', '예상', '출발', '구분', '현황']
from_col = ['날짜', '항공사', '편명', '도착', '계획', '예상', '출발', '구분', '현황']


def parsing_csv(origin_file_path, new_file_path, column):
    new_df = pd.DataFrame(columns=column)  # 새로운 df 생성 (새로 저장할 csv)
    origin = pd.read_csv(origin_file_path, encoding='CP949')

    count = 0
    error_count = 0
    for j in range(len(origin)):
        row = origin.loc[j]  # 날짜에 따른 row (항공기 여러개 선택) 0: 1번째 날짜
        for i in range(1, len(row)):
            try:
                try:
                    temp = row[i][1:-1].split(', ')
                    new_df.loc[count] = temp
                    count += 1
                except ValueError:
                    error_count += 1
            except TypeError:
                pass

    print(error_count)
    new_df.to_csv(new_file_path, encoding='utf-8-sig')


# parsing_csv('제주출발.csv', 'new_csv/Flight_From_CJU.csv', from_col)
# parsing_csv('김포출발.csv', 'new_csv/Flight_From_GMP.csv', from_col)
# parsing_csv('제주도착.csv', 'new_csv/Flight_to_CJU.csv', to_col)
# parsing_csv('김포도착.csv', 'new_csv/Flight_to_GMP.csv', to_col)
