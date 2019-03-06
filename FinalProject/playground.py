import pandas as pd
from datetime import date

df = pd.read_csv("./kickstarter-projects/ks-projects-201801.csv")
df = df.drop(columns=["ID", "usd pledged", "pledged", "currency", "name", "goal"])
df = df.rename(columns={"usd_pledged_real": "pledged", "usd_goal_real": "goal"})
df['launched'] = df['launched'].apply(lambda x: x.split(' ')[0])
df = df.dropna()

def date_difference_days(date1, date2):
    print(date1, date2)
    split_components = lambda d: list(map(int, d.split('-')))
    
    d1, d2 = split_components(date1), split_components(date2)
    launched = date(d1[0], d1[1], d1[2])
    deadline = date(d2[0], d2[1], d2[2])

    return (deadline - launched).days

df.head()