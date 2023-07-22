import numpy as np
import matplotlib.pyplot as plt

class DFT:
    def __init__(self, stock = "C:/Users/mauri/Downloads/TGT.csv", x=[0, 1, 0, -1, 0, 1, 0, -1], t=np.linspace(0,8),
                 timespace = [0, 1, 2, 3, 4, 5, 6, 7], interval=[0, 8], color = "red", name="line"):
        self.stock = stock
        self.x = x
        self.t = t
        self.interval = interval
        self.color = color
        self.timespace = timespace
        self.name = name

    def myfunc(self):
        plt.scatter(self.timespace, self.x, c=self.color)
        n = len(self.x)
        w = np.eye(n)

        matrix = np.empty((n, n), dtype=complex)
        for i in range(0,n):
            for k in range(0,n):
                l = i*k
                a = np.cos((2*np.pi*l)/n)
                b = np.sin((2*np.pi*l)/n)
                ans = a - b*1j
                matrix[i][k] = ans

        #print("This is the DFT matrix: ", matrix)

        y = (1/np.sqrt(n))*(np.matmul(matrix, self.x))
        #print("This is my y matrix: ",y)

        a_matrix = []
        b_matrix = []
        for i in range(0,len(y)):
            a_matrix.append(y[i].real)
            b_matrix.append(y[i].imag)

        #print(a_matrix)
        #print(b_matrix)
        eq= a_matrix[0]/(np.sqrt(n))
        #print(eq)
        h = int(n/2)
        marker = int((n/2)-1)
        #print("marker: ", marker)
        inter = self.interval[1]-self.interval[0]
        #print(marker)
        if marker != 1:
            # the calculations are messing up right here
            for j in range(1,marker+1):
                #print("me")
                eq += (2/np.sqrt(n))*(a_matrix[j] * np.cos( (2*np.pi*j*(self.t-self.interval[0])) / inter) -
                                b_matrix[j] * np.sin((2*np.pi*j*(self.t-self.interval[0])) / inter))
        else:
            print("passing here")
            eq += (2/np.sqrt(n))*(a_matrix[1] * np.cos((2*np.pi*1*(self.t-self.interval[0])) / inter) -
                                  b_matrix[1] * np.sin((2*np.pi*1*(self.t-self.interval[0])) / inter))

        eq += (a_matrix[h]/np.sqrt(n)) * np.cos(n*np.pi*(self.t-self.interval[0]) / inter)
        plt.plot(self.t, eq, c=self.color, label=self.name)