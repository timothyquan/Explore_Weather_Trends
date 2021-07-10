import pandas as pd 
import numpy as np
import matplotlib.pyplot as plot

#########
#Config#
#########
city_data_path = "./csv/bangkok_data.csv"
global_data_path = "./csv/global_data.csv"
rwindow = 5 #the 'window' for rolling data
########


if __name__ == "__main__":
    #import the .csv files to dataframes
    city_df = pd.read_csv(city_data_path)
    glbl_df = pd.read_csv(global_data_path)
    city_name = label=city_df.at[2, 'city']

    

    #calculate the rolling average for both dataframes
    city_df['avg_temp_rolling'] = city_df.rolling(window=rwindow)['avg_temp'].mean().dropna()
    glbl_df['avg_temp_rolling'] = glbl_df.rolling(window=rwindow)['avg_temp'].mean().dropna()

    #use pyplot to generate line graph
    plot.grid(True)
    plot.plot(city_df['year'], city_df['avg_temp_rolling'], label=city_name)
    plot.plot(glbl_df['year'], glbl_df['avg_temp_rolling'], label='Global')
    plot.ylabel('Degrees Celcius')
    plot.xlabel('Year')
    plot.title(f"{city_name} vs. Global"
        f"\n {rwindow} year rolling average temperatures")
    plot.legend()
    plot.show()   
