import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    df = pd.read_csv('NetflixOriginals.csv', encoding='ISO-8859-1')

    sns.heatmap(df[["IMDB Score", "Runtime"]].corr(), annot=True)
    plt.title('Correlation')
    plt.show()

    print("\nAs observed from heatmap, there is no significant correlation between IMDB Score and Runtime.\n")
