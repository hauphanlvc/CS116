from matplotlib import colors
from numpy.core.numeric import correlate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

data = pd.read_csv("excel_vnm.csv")
print(data.describe())
print(data.head())
# print(data["<Volume>"])
# volume  = np.array(data["<Volume>"][::-1])
volume  = np.array(data["<Volume>"])
# price = np.array(data["<CloseFixed>"][::-1])
# time = np.array(data["<DTYYYYMMDD>"][::-1])
price = np.array(data["<CloseFixed>"])
# price = price[::-1]
# time = np.array(data["<DTYYYYMMDD>"][::-1])
time = np.array(data["<DTYYYYMMDD>"])
fig, ax1= plt.subplots()
ax1.set_xlabel("Time")
ax1.set_ylabel("Price data", color = 'red')
ax1.plot(price , color = 'red')

ax2 = ax1.twinx()

ax2.set_ylabel("Volume data",color = 'blue')
# ax2.plot(time,volume)
ax2.plot(volume, color = 'blue')
plt.show() 
