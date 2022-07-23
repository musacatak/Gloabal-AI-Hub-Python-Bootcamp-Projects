import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    pdDf = pd.read_csv('NetflixOriginals.csv', encoding='latin-1')
    df1 = pdDf[['Language', "Genre"]]
    a = df1.groupby(['Language']).agg(mod=('Genre',
                                           lambda x: x.value_counts().index[0])
                                      )
    print(a)
