import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    pdDf = pd.read_csv('NetflixOriginals.csv', encoding='latin-1')

    df1 = pdDf[['Language', "IMDB Score"]]
    a = df1.groupby(['Language'])['IMDB Score'].mean().to_frame('Avg IMDB Score')
    x = a.index.tolist()
    z = a.values.tolist()
    y = []
    for i in range(len(z)):
        y.append(z[i][0])
    print("\nThe language that has the smallest IMDB Score is", x[y.index(min(y))], "with", min(y), "points.\n")
    fig = plt.figure(figsize=(10, 7))
    plt.barh(x, y)
    plt.show()

