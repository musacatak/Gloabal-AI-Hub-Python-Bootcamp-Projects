import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    pdDf = pd.read_csv('NetflixOriginals.csv', encoding='latin-1')

    # pdDf.to_csv("NetflixOriginals.csv", index=False)
    z = pdDf['Genre'].count()
    x = pdDf['Genre'].value_counts(ascending=True)

    y = x.values.tolist()
    x = x.keys().tolist()
    fig = plt.figure(figsize=(40, 28))
    expl = []
    c = 0.1
    for i in range(len(x)):
        expl.append(c)
        c += 0.001

    def func(pct, allvalues):
        absolute = int(pct / 100. * np.sum(allvalues))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    plt.pie(y, labels=x, explode=expl, autopct=lambda pct: func(pct, y))
    plt.legend(x, title="Genres",
               loc='upper right')
    # show plot
    print("There are ", z, "kind Genres in dataset and these Genres are:")
    for i in x:
        print(i)
    plt.show()
main()