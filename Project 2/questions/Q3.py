import pandas as pd
import matplotlib.pyplot as plt


def main():
    pdDf = pd.read_csv('NetflixOriginals.csv', encoding='latin-1')
    y = pdDf['IMDB Score'][(pdDf['Language'] == 'English') & (pdDf['IMDB Score'] == pdDf['IMDB Score'].max())]
    x = pdDf['Genre'][(pdDf['Language'] == 'English') & (pdDf['IMDB Score'] == pdDf['IMDB Score'].max())]

    y = y.tolist()
    x = x.tolist()

    print("\nThe highest IMDB score among movies made in English is", x[0], "\n")

