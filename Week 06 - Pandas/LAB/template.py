"""
RECORD CHECK  -  my version
===========================

Name  : Bhavya 
Lane  :  AI 
Date  : 5/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt


data = {
    "label": ["A", "B", "C", "D", "E"],
    "value": [80, 95, 110, 65, 90],
    "limit": [100, 100, 100, 100, 100]
}


df1 = pd.DataFrame(data)
df1.to_csv("data.csv", index=False)

df = pd.read_csv("data.csv")


df["percent"] = (df["value"] / df["limit"]) * 100


df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x >= 100 else
    "WARNING" if x >= 90 else "OK"
)

print("Complete Data:")
print(df)

print("\nData which needs attention:")
print(df[df["status"] != "OK"])


count = df.groupby("status").size()

print("\nStatus Count:")
print(count)


df.to_csv("output.csv", index=False)


count.plot(kind="bar")

plt.title("Status Count")
plt.xlabel("Status")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("status_chart.png")
plt.show()

print("\nFirst row:")
print(df.iloc[0])
