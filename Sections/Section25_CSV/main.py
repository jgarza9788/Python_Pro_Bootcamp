
import os
import pandas as pd
DIR = os.path.dirname(os.path.realpath(__file__))

def show_weather_data():
    """
    just converts the wd.csv (weather data) into a dataframe
    """
    df = pd.read_csv(os.path.join(DIR,'wd.csv'))
    print(df)


def squirrel_count():
    """
    some project using 2018_Central_Park_Squirrel_Census_Squirrel_Data.csv data
    """

    df = pd.read_csv(os.path.join(DIR,'2018_Central_Park_Squirrel_Census_Squirrel_Data.csv'))
    
    df = df.rename(columns={"Primary Fur Color": "FurrColor"})
    df = df.rename(columns={"Unique Squirrel ID": "Count"})

    df = df[['FurrColor','Count']].groupby(
        ['FurrColor']
    ).count()

    df.to_csv(os.path.join(DIR,'squirrel_count.csv'))
    print(df)



if __name__ == '__main__':
    # show_weather_data()
    squirrel_count()