import datetime
import pandas as pd
import matplotlib.pyplot as plt


def main():
    pdDf = pd.read_csv('NetflixOriginals.csv', encoding='latin-1')
    bD = datetime.datetime(2019, 1, 1)
    aD = datetime.datetime(2020, 6, 30)
    format_date_data = "%B %d, %Y"
    for i in range(len(pdDf['Premiere'])):
        try:
            pdDf.loc[i, 'Premiere'] = datetime.datetime.strptime(pdDf['Premiere'][i], format_date_data)
        except ValueError:
            pdDf.loc[i, 'Premiere'] = datetime.datetime.strptime(pdDf['Premiere'][i], "%B %d. %Y")

    # pdDf.to_csv("NetflixOriginals.csv", index=False)
    y = pdDf['IMDB Score'][(pdDf['Genre'] == 'Documentary') & (pdDf['Premiere'] < aD) & (pdDf['Premiere'] > bD)]
    x = pdDf['Title'][(pdDf['Genre'] == 'Documentary') & (pdDf['Premiere'] < aD) & (pdDf['Premiere'] > bD)]

    y = y.tolist()
    x = x.tolist()
    plt.figure(figsize=(19.2, 10.8))
    plt.barh(x, y)
    plt.title("01.01.2019 - 31.06.2020 Films Genre = Documentary")
    plt.xlabel("IMDB Scores")
    plt.show()