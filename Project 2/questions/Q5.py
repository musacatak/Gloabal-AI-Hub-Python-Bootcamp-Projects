import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv('NetflixOriginals.csv', encoding='ISO-8859-1')

    print("\nNumber of Genre categories is", df["Genre"].nunique(), "\n")
    genre_df = df["Genre"].value_counts()

    # It cannot be plotted with all genre categories due to having 115 categories, so top 20 categories was chosen.
    new_genre_df = df["Genre"].value_counts().nlargest(20)
    plt.barh(new_genre_df.index, new_genre_df.values)
    plt.title("Top 20 Genres vs Number of Movies ")
    plt.ylabel("Categories")
    plt.xlabel("Number of the movies")
    plt.show()
