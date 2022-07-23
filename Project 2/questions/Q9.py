import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    pdDf = pd.read_csv('NetflixOriginals.csv', encoding='latin-1')
    
    df1 = pdDf[['Genre', "IMDB Score"]]
    df2 = df1.groupby(['Genre']).max()['IMDB Score'].nlargest(10)
    x = df2.values
    y = df2.keys()
    plt.scatter(x, y, color="orange")
    plt.title("TOP 1O MOVIES ACCORDING TO IMDB SCORES")
    plt.xlabel("IMDB Scores")
    plt.ylabel("Movies")
    plt.show()
