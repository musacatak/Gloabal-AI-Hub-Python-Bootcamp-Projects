import pandas as pd
import matplotlib.pyplot as plt


def main():
    pdDf = pd.read_csv('NetflixOriginals.csv', encoding='latin-1')
    y1 = pdDf['IMDB Score'].head(10)
    y2 = pdDf['Runtime'].head(10)
    x = pdDf['Title'].head(10)
    y2 = y2.tolist()
    for i in range(len(y2)):
        y2[i] /= 10
    plt.plot(x, y1, label='IMDB Score')
    plt.plot(x, y2, label='Runtime')
    plt.legend()
    plt.show()

