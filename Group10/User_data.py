import pandas as pd
import os

def data_to_csv():

    df=pd.DataFrame(columns=['Name','Email','Age','Gender','Major',''])
    print(df)
    df.to_csv('./user_data/test.csv',index=False)


data_to_csv()
