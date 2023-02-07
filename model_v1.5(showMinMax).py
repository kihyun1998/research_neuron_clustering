import csv
import pandas as pd


data1 = pd.read_csv("rec1.csv", header=None, names=["t", "v"])
data2 = pd.read_csv("rec2.csv", header=None, names=["t", "v"])
data3 = pd.read_csv("rec3.csv", header=None, names=["t", "v"])

print(f"soma(0.5) : \n {data1['v'].max()}, {data1['v'].min()}")
print(f"apic[11](0.5) : \n {data2['v'].max()}, {data2['v'].min()}")
print(f"apic[49](0.5) : \n {data3['v'].max()}, {data3['v'].min()}")