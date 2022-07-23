import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def func(pct, all_values):
    absolute = int(pct / 100. * np.sum(all_values))
    return "{:.1f}%\n({:d})".format(pct, absolute)

def main():
    pdDf = pd.read_csv('NetflixOriginals.csv', encoding='latin-1')
    y = pdDf['Runtime'].nlargest(n=10)
    z = y.values.tolist()
    x = y.keys().tolist()
    for i in range(len(x)):
        a = pdDf.loc[x[i], 'Title']
        x[i] = a
    print("First 10 movies having highest runtime\n")
    for i in range(len(x)):
        print(i+1, ":", x[i])
    print()
    plt.figure(figsize=(10, 10))
    expl = []
    c = 0.1
    for i in range(len(x)):
        expl.append(c)
        c += 0.001


    plt.pie(y, labels=x, explode=expl, autopct=lambda pct: func(pct, y))
    plt.legend(x, title="Movie Titles",
               loc='center')
    # show plot
    plt.show()
