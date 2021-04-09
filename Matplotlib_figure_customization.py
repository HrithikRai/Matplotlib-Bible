import matplotlib.pyplot as plt
import pandas as pd

# Scatter Plot --> marker,color,size
plt.subplot(2,3,1)
df2 = pd.read_csv("salesdata2.csv",header=None)
df2.columns = ["sales","cost"]
plt.title("Sales vs Cost")
plt.xlabel("Sales")
plt.ylabel("Cost")
plt.scatter(list(df2.sales),list(df2.cost),marker="*",s=100,c='r')

# Boxplot --> patch_artist
plt.subplot(2,3,2)
sales = []
file = open('salesdata.csv')
salesfile = file.readlines()

for records in salesfile:
    sales.append(int(records))
    
plt.title("Sales Boxplot")
plt.boxplot(sales,patch_artist=True)

# Histogram --> color
plt.subplot(2,3,3)
data = []
f = open("agedata.csv",'r')
agefile = f.readlines()

for records in agefile:
    data.append(int(records))
    
bins = [10,20,30,40,50,60,70,80,90,100]

plt.title('Age Histogram')
plt.xlabel("Age")
plt.ylabel("groups")

plt.hist(data,bins,histtype='bar',rwidth=0.5,color='c')

# Line Plot --> color,marker,markersize,linewidth,linestyle
plt.subplot(2,3,4)
x_days = [1,2,3,4,5]
y_stock1 = [10,11,10.5,13,14]
y_stock2 = [11,13,12.5,13,15]

plt.title('Stock Prices')
plt.xlabel("Days")
plt.ylabel("Prices")

plt.plot(x_days,y_stock1,label='Stock 1',color='green',marker='o',markersize=10,linewidth=3,linestyle='--')

plt.plot(x_days,y_stock2,label='Stock 2',color='red',marker='D',markersize=10,linewidth=3,linestyle='--')

plt.legend(loc=2,fontsize=10)

# Bar Chart --> color
plt.subplot(2,3,5)
x_cities = ['London','paris','New York','New Delhi','Tokyo']
y_temp = [23,30,25,36,22]

plt.title('City Temperatures')
plt.xlabel("Cities")
plt.ylabel("Temps")

plt.bar(x_cities,y_temp,color=['r','g','c','y','m'])

plt.tight_layout()
plt.plot()
