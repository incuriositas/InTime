import pandas as pd
import IntimeLib as il

__df_from_cju = pd.read_csv("dataset/SortedCSV/Flight_from_CJU(Sorted).csv")
__df_from_gmp = pd.read_csv("dataset/SortedCSV/Flight_from_GMP(Sorted).csv")
__df_to_cju = pd.read_csv("dataset/SortedCSV/Flight_to_CJU(Sorted).csv")
__df_to_gmp = pd.read_csv("dataset/SortedCSV/Flight_to_GMP(Sorted).csv")

__weather_gmp_10 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201810.csv")
__weather_cju_10 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201810.csv")
__weather_gmp_11 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201811.csv")
__weather_cju_11 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201811.csv")
__weather_gmp_12 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201812.csv")
__weather_cju_12 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201812.csv")
__weather_gmp_01 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201901.csv")
__weather_cju_01 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201901.csv")
__weather_gmp_02 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201902.csv")
__weather_cju_02 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201902.csv")
__weather_gmp_03 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201903.csv")
__weather_cju_03 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201903.csv")
__weather_gmp_04 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201904.csv")
__weather_cju_04 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201904.csv")
__weather_gmp_05 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201905.csv")
__weather_cju_05 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201905.csv")
__weather_gmp_06 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201906.csv")
__weather_cju_06 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201906.csv")
__weather_gmp_07 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201907.csv")
__weather_cju_07 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201907.csv")
__weather_gmp_08 = pd.read_csv("dataset/WeatherCSV/김포공항/RKSS_air_stcs201908.csv")
__weather_cju_08 = pd.read_csv("dataset/WeatherCSV/제주공항/RKPC_air_stcs201908.csv")

weather_cju = [__weather_cju_10,
               __weather_cju_11,
               __weather_cju_12,
               __weather_cju_01,
               __weather_cju_02,
               __weather_cju_03,
               __weather_cju_04,
               __weather_cju_05,
               __weather_cju_06,
               __weather_cju_07,
               __weather_cju_08]
weather_gmp = [__weather_gmp_10,
               __weather_gmp_11,
               __weather_gmp_12,
               __weather_gmp_01,
               __weather_gmp_02,
               __weather_gmp_03,
               __weather_gmp_04,
               __weather_gmp_05,
               __weather_gmp_06,
               __weather_gmp_07,
               __weather_gmp_08]


il.fix_flight(__df_from_cju, 0)
il.fix_flight(__df_from_gmp, 0)
il.fix_flight(__df_to_cju, 1)
il.fix_flight(__df_to_gmp, 1)

# fix_time(df_from_cju, "from_cju.csv")
# fix_time(df_from_gmp, "from_gmp.csv")
# fix_time(df_to_cju, "to_cju.csv")
# fix_time(df_to_gmp, "to_gmp.csv")

flight_from_cju = pd.read_csv("dataset/FlightCSV/from_cju.csv")
flight_from_cju.drop("Unnamed: 0", axis=1, inplace=True)
flight_from_gmp = pd.read_csv("dataset/FlightCSV/from_gmp.csv")
flight_from_gmp.drop("Unnamed: 0", axis=1, inplace=True)
flight_to_cju = pd.read_csv("dataset/FlightCSV/to_cju.csv")
flight_to_cju.drop("Unnamed: 0", axis=1, inplace=True)
flight_to_gmp = pd.read_csv("dataset/FlightCSV/to_gmp.csv")
flight_to_gmp.drop("Unnamed: 0", axis=1, inplace=True)

for i in range(len(weather_cju)):
    il.fix_weather(weather_cju[i])
    il.fix_weather(weather_gmp[i])
