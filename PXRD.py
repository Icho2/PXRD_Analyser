import pandas as pd
import matplotlib.pyplot as plt

# Just replace the path for your .csv file's path
comp = input("Mac or Windows? (m/w) ")
path = input("Enter file path: ")  # make sure to get rid of the quaotations in your input
include = input("Enter what graphs you want to see (for all type all): ")
title = input("Enter title: ")
color = input("Do you want to color code your graphs? (y/n) ")

if (path == "example"):
    path = 'C:/Users/mauri/OneDrive/Desktop/Humphrey_Lab/Ben Siu/ligand.csv'
elif (path != "example" and comp == "w"):
    path = path.replace('\\', '/')
    path = path.replace('"', '')

# hard-coded variables
data = pd.read_csv(open(path), sep=',')
x = data[data.columns[0]]
translation = 0
used_colors = {}

if include == "all":
    graphs = []
    for i in range(0, (len(data.columns)//2)):
        graphs.append(2*i + 1)
else:
    include = include.split()
    include = [eval(i) for i in include]
    graphs = []
    for i in include:
        n = (i * 2) - 1
        graphs.append(n)

for i in graphs:
    if color == 'n':
        col = data.columns[i]
        y = abs(min(data[col])) + data[col]
        z = y / (max(y)) + translation
        translation += 1.5
        plt.plot(x, z, label=data.columns[i - 1])
    elif color == 'y':
        col = data.columns[i]
        y = abs(min(data[col])) + data[col]
        z = y / (max(y)) + translation
        translation += 1.5
        print("Used colors: ", used_colors)
        paint = input("Enter color for graph " + data.columns[i - 1] + " : ")
        used_colors[data.columns[i - 1]] = paint
        plt.plot(x, z, label=data.columns[i - 1], c=paint)

plt.title(title)
plt.legend()
plt.show()