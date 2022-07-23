import pandas as pd


def main():
    pdDf = pd.read_csv('NetflixOriginals.csv', encoding='latin-1')
    y = pdDf['Runtime'][(pdDf['Language'] == 'Hindi')].mean()
    x = pdDf['Runtime'][(pdDf['Language'] == 'Hindi')].count()

    print('\nThere are ', x, 'times movie ,that language is Hindi, and their avg Runtime is :', y, "\n")
