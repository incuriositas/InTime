import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def mask_with_in1d(df, column, val):
    mask = np.in1d(df[column].values, [val])
    return df[mask]


def one_hot(df, cols):
    new_df = pd.get_dummies(df, columns=cols)
    return new_df


def fix_flight(df, i):
    if i == 0:
        df.drop(["Unnamed: 0", "편명", "목적지",  "예상", "구분"], axis=1, inplace=True)
    else:
        df.drop(["Unnamed: 0", "편명", "출발지", "예상", "구분"], axis=1, inplace=True)

def fix_time(df):
    for i in range(len(df)):
        if len(df['time'][i]) < 1:
            df['TM'] = str(df['날짜']) + str(0) + df['계획'].str.split(':').str[0]
        else:
            df['TM'] = str(df['날짜']) + df['계획'].str.split(':').str[0]

def fix_weather(df):
    df['Date'] = df.TM.apply(lambda x: str(x)[:8])
    df['Time'] = df.TM.apply(lambda x: str(x)[8:])


df_from_cju = pd.read_csv("dataset/SortedCSV/Flight_from_CJU(Sorted).csv")
df_from_gmp = pd.read_csv("dataset/SortedCSV/Flight_from_GMP(Sorted).csv")
df_to_cju = pd.read_csv("dataset/SortedCSV/Flight_to_CJU(Sorted).csv")
df_to_gmp = pd.read_csv("dataset/SortedCSV/Flight_to_GMP(Sorted).csv")

weather_gmp_10 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201810.csv")
weather_cju_10 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201810.csv")
weather_gmp_11 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201811.csv")
weather_cju_11 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201811.csv")
weather_gmp_12 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201812.csv")
weather_cju_12 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201812.csv")
weather_gmp_01 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201901.csv")
weather_cju_01 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201901.csv")
weather_gmp_02 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201902.csv")
weather_cju_02 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201902.csv")
weather_gmp_03 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201903.csv")
weather_cju_03 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201903.csv")
weather_gmp_04 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201904.csv")
weather_cju_04 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201904.csv")
weather_gmp_05 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201905.csv")
weather_cju_05 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201905.csv")
weather_gmp_06 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201906.csv")
weather_cju_06 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201906.csv")
weather_gmp_07 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201907.csv")
weather_cju_07 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201907.csv")
weather_gmp_08 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201908.csv")
weather_cju_08 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201908.csv")


fix_flight(df_from_cju, 0)
fix_flight(df_from_gmp, 0)
fix_flight(df_to_cju, 1)
fix_flight(df_to_gmp, 1)

fix_time(df_from_cju)
fix_time(df_from_gmp)
fix_time(df_to_cju)
fix_time(df_to_gmp)

fix_weather(weather_gmp_10)
fix_weather(weather_cju_10)
fix_weather(weather_gmp_11)
fix_weather(weather_cju_11)
fix_weather(weather_gmp_12)
fix_weather(weather_cju_12)
fix_weather(weather_gmp_01)
fix_weather(weather_cju_01)
fix_weather(weather_gmp_02)
fix_weather(weather_cju_02)
fix_weather(weather_gmp_03)
fix_weather(weather_cju_03)
fix_weather(weather_gmp_04)
fix_weather(weather_cju_04)
fix_weather(weather_gmp_05)
fix_weather(weather_cju_05)
fix_weather(weather_gmp_06)
fix_weather(weather_cju_06)
fix_weather(weather_gmp_07)
fix_weather(weather_cju_07)
fix_weather(weather_gmp_08)
fix_weather(weather_cju_08)
