import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def mask_with_in1d(df, column, val):
    mask = np.in1d(df[column].values, [val])
    return df[mask]


def one_hot(df, col):
    new_col = pd.get_dummies(df[col])
    return new_col


df_from_cju = pd.read_csv("dataset/SortedCSV/Flight_from_CJU(Sorted).csv")
df_from_gmp = pd.read_csv("dataset/SortedCSV/Flight_from_GMP(Sorted).csv")
df_to_cju = pd.read_csv("dataset/SortedCSV/Flight_to_CJU(Sorted).csv")
df_to_gmp = pd.read_csv("dataset/SortedCSV/Flight_to_GMP(Sorted).csv")

df_gmp_10 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201810.csv")