import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("God_Stats+.csv", index_col=0)


def make_list(name):
    temp = list()
    temp.append(name)
    temp.append(name + " PL")
    number = ["1", "3", "5", "10", "20"]
    for num in number:
        temp.append(name + " " + num)

    temp.append("Class")
    return temp


print(df.describe())
columns = ["Health", "Mana", "Pysical Prot", "Magical Prot", "HP5", "MP5", "Basic Attack Damage", "Attack Speed"]
charts = list()
for column in columns:
    column = df[make_list(column)]
    charts.append(column)

print(charts)
print(type(charts[0]))
print(columns)
print(list(df.columns))

#plot the general stats as a pair plot
#for x in charts:
    #sns.pairplot(x, hue="Class")


#sets the date to a workable one and creats a sorted dataset
df['Release Date'] =pd.to_datetime(df["Release Date"])
dff = df.sort_values(by = "Release Date")

#plots lineplots
#sns.lineplot(data = dff["Pysical Prot"])

sns.heatmap(data = dff[columns] )

plt.show()
