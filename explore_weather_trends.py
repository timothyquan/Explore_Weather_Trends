import pandas as pd 
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
    #putting extracted city name in variable
    city_temp_string = f"{city_df.at[2, 'city']}_avg_temp_rolling"

    #calculate the rolling average for both dataframes
    city_df[city_temp_string] = city_df.rolling(window=rwindow)["avg_temp"].mean()
    glbl_df["global_avg_temp_rolling"] = glbl_df.rolling(window=rwindow)["avg_temp"].mean()

    #merge the two dataframes 
    merged_df = pd.merge(glbl_df.loc[:, ["year", "global_avg_temp_rolling"]], \
        city_df.loc[:, ["year", city_temp_string]],\
            on = "year", how="outer"
    )

    #use pyplot to generate line graph
    merged_df.plot.line(x="year", y=[city_temp_string, "global_avg_temp_rolling"])
    plot.ylabel('Degrees Celcius')
    plot.show()   
