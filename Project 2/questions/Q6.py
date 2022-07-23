import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    pdDf = pd.read_csv('NetflixOriginals.csv', encoding='latin-1')

    # pdDf.to_csv("NetflixOriginals.csv", index=False)
    n = 3
    x = pdDf['Language'].value_counts()[:n]
    print("\n", x, "\n")
    y = x.values.tolist()
    x = x.keys().tolist()

    fig = plt.figure(figsize=(10, 7))
    expl = []
    c = 0.1
    for i in range(len(x)):
        expl.append(c)
        c += 0.001

    def func(pct, all_values):
        absolute = int(pct / 100. * np.sum(all_values))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    plt.pie(y, labels=x, explode=expl, autopct=lambda pct: func(pct, y))
    plt.legend(x, title="Languages",
               loc='upper right')
    # show plot
    plt.show()
