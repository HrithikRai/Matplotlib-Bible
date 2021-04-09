# Constructing Simple Plots using matplotlib

## Numerical Data

# Line Chart
import matplotlib.pyplot as plt


x_days = [1,2,3,4,5]
y_stock1 = [10,11,10.5,13,14]
y_stock2 = [11,13,12.5,13,15]

plt.title('Stock Prices')
plt.xlabel("Days")
plt.ylabel("Prices")

plt.plot(x_days,y_stock1,label='Stock 1')

plt.plot(x_days,y_stock2,label='Stock 2')

plt.legend(loc=2,fontsize=10)
plt.show()

# Bar Graph
import matplotlib.pyplot as plt2

x_cities = ['London','paris','New York','New Delhi','Tokyo']
y_temp = [23,30,25,36,22]

plt2.title('City Temperatures')
plt2.xlabel("Cities")
plt2.ylabel("Temps")

plt2.bar(x_cities,y_temp)
plt2.plot()

# Histogram - Pictorial Representation of the Frequency Chart
import matplotlib.pyplot as plt3

data = []
f = open(r"C:\Users\MSI\Desktop\Data Science\agedata.csv",'r')
agefile = f.readlines()

for records in agefile:
    data.append(int(records))
    
bins = [10,20,30,40,50,60,70,80,90,100]

plt3.title('Age Histogram')
plt3.xlabel("Age")
plt3.ylabel("groups")

plt3.hist(data,bins,histtype='bar',rwidth=0.5)
plt3.show()

# BoxPlot- A figure giving us the Inter Quartile range with median and outliers
import matplotlib.pyplot as plt4

sales = []
file = open(r'C:/Users/MSI/Desktop/Data Science/salesdata.csv')
salesfile = file.readlines()

for records in salesfile:
    sales.append(int(records))
    
plt4.title("Sales Boxplot")
plt4.boxplot(sales)
plt4.show()

## Categorical Data

# Pie Chart
import matplotlib.pyplot as plt5
import pandas as pd

df = pd.read_csv("agedata2.csv")
df.columns = ['age','city']

x = list(df.groupby('city').age.count()) # first create groups and then do the operations
y = list(df.city.sort_values().unique())

plt5.title("Pie Chart of Age distribution among cities")
plt5.pie(x,labels=y,autopct='%.2f%%')
plt5.show()

# Scatter Plot
import matplotlib.pyplot as plt6

df2 = pd.read_csv("salesdata2.csv",header=None)
df2.columns = ["sales","cost"]

plt6.title("Sales vs Cost")
plt6.xlabel("Sales")
plt6.ylabel("Cost")

plt6.scatter(list(df2.sales),list(df2.cost))
plt6.show()

# Multiple Plots in a Single Figure...

import matplotlib.pyplot as plt7

x = [1,4,3,5,6,5,7,10]
y = [4,5,6,2,5,7,7,18]

plt7.subplot(2,2,1)
plt7.title("Scatter")
plt7.scatter(x,y)

plt7.subplot(2,2,2)
plt7.title("Histogram")
bins = [1,5,10,15]
plt7.hist(x+y,bins,histtype="bar",rwidth=0.5)

plt7.tight_layout() # To get a neat figure without overlapping charts...
plt7.show()







