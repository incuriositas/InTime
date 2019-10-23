import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import matplotlib.font_manager as fm
fm.get_fontconfig_fonts()
# font_location = '/usr/share/fonts/truetype/nanum/NanumGothicOTF.ttf'
font_location = 'Arial Unicode.ttf' # For Windows
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)


def display_heatmap(df):
    plt.figure(figsize=(10, 7))
    sns.heatmap(df.corr(),annot=True ,cmap='cubehelix_r')
    plt.show()


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


def fix_time(df, file_name):
    df['time'] = df['계획'].str.split(':').str[0]
    df['TM'] = ""
    for i in range(len(df)):
        if len(df['time'][i]) == 1:
            df['TM'][i] = str(df['날짜'][i]) + "0" + df['time'][i]
            print(df['TM'][i])
        else:
            df['TM'][i] = str(df['날짜'][i]) + df['time'][i]
    df.to_csv("dataset/FlightCSV/"+file_name, encoding='utf-8-sig')


def fix_weather(df):
    df['Date'] = df.TM.apply(lambda x: str(x)[:8])
    df['Time'] = df.TM.apply(lambda x: str(x)[8:])


def month_slice(df, day, last):
    new_df = pd.DataFrame()
    for i in range(last):
        temp = mask_with_in1d(df, "날짜", day)
        new_df = pd.concat([new_df, temp], ignore_index=True)
        day += 1
    return new_df
