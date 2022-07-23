import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    pdDf = pd.read_csv('NetflixOriginals.csv', encoding='latin-1')
    y = pdDf['IMDB Score'].nlargest(n=10)
    z = y.values.tolist()
    x = y.keys().tolist()
    for i in range(len(x)):
        a = pdDf.loc[x[i], 'Title']
        x[i] = a
    print("\nFirst 10 movies having highest IMDB score:\n")
    for i in range(len(x)):
        print(i+1,":",x[i])
    print()
    plt.figure(figsize=(10,  10))
    expl = []
    c = 0.1
    for i in range(len(x)):
        expl.append(c)
        c += 0.001

    def func(pct, all_values):
        absolute = float(pct / 100. * np.sum(all_values))
        return "{:.1f}%\n({:.1f})".format(pct, absolute)

    plt.pie(z, labels=x, explode=expl, autopct=lambda pct: func(pct, z))
    plt.title("First 10 movies having highest IMDB score")
    plt.legend(x, title="Top 10 IMDB Score",
               loc='center')
    # show plot
    plt.show()