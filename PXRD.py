import pandas as pd
import matplotlib.pyplot as plt

#Just replace the path for your .csv file's path
path = input("Enter file path: ") #make sure to get rid of the quaotations in your input
include = input("Enter what graphs you want to see (for all type all): ")

if (path == "example"):
    path = "C:/Users/Mauricio/Desktop/MOFs/PXRD/Excel_files/ligand.csv"
data = pd.read_csv(open(path), sep=',')
x = data[data.columns[0]]
translation = 0
if include == "all":
    include = list(range(0,len(data.columns)+1))
else:
    include = include.split()
    #include = list(include, sep=' ')
print(include)
for i in include:
    if (i % 2 != 0):
        col = data.columns[i]
        y = abs(min(data[col])) + data[col]
        z = y/(max(y)) + translation
        translation+=1.5
        plt.plot(x, z, label=data.columns[i-1])
plt.title("samples")
plt.legend()
plt.show()