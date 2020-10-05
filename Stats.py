import numpy as np
import pandas as pd

df = pd.read_csv("God_Stats.csv", index_col = 0)

def Level_Calc(x, y, z):
    a = x + y*z
    return a

def Attack_Speed(x, y, z):
    a = x*(1 +((y/100)*z))
    return a



columns = ["Health", "Mana", "Pysical Prot", "Magical Prot", "MP5", "HP5", "Basic Attack Damage"]
levels = [1, 3, 5, 10, 20]

for x in columns:
    for y in levels:
        df[(x + " " + str(y))] = Level_Calc(df[x], df[x + " PL"], y)

mod = df['Attack Speed PL'].str[:-1].astype(float)
print(mod)

for y in levels:
    df["Attack Speed" + " "+ str(y)] = Attack_Speed(df["Attack Speed"], mod, y)


print(df)
df.to_csv('God_Stats+.csv')