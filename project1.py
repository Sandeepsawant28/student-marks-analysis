import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('marks.csv')
print(df)
df["Total"]=df[["Maths","Science","English"]].sum(axis=1)
df["Average"]=df["Total"]/3
print(df)
topper_index = df["Total"].idxmax()
topper_name = df.loc[topper_index, "Name"]
print("\nTopper:\n",topper_name)
colors = ["red" if i == topper_index else "blue" for i in df.index]
plt.bar(df["Name"], df["Total"], color=colors)
plt.title("Total Marks of Students")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.show()