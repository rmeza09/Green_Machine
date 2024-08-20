
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import csv
import pandas as pd

dataSheet = pd.read_csv(r"C:\\Users\\rmez1\\OneDrive\\Desktop\\StockAnalysis\\02 - Data\\AAPL.csv")

dataSheet['Date'] = pd.to_datetime(dataSheet['Date'])

plt.figure(1, figsize=(10, 6))
plt.plot(dataSheet['Date'], dataSheet['Close'], label='Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Close Prices Over Time')
plt.legend()
plt.grid(True)


plt.figure(2, figsize=(10, 6))
plt.plot(dataSheet['Date'], dataSheet['Open'], label='Open Price')
plt.plot(dataSheet['Date'], dataSheet['Close'], label='Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Open and Close Prices Over Time')
plt.legend()
plt.grid(True)


plt.figure(3, figsize=(10, 6))
plt.bar(dataSheet['Date'], dataSheet['Volume'], label='Volume', color='orange')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.title('Trading Volume Over Time')
plt.legend()
plt.grid(True)


plt.show()


#sorry
#x = np.linspace(0, 20, 100)
#plt.plot(x, np.sin(x))
#plt.show()

  

