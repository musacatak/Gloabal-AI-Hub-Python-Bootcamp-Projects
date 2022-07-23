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
    df1 = pdDf[['Premiere', 'Runtime']]
    for i in range(len(df1['Premiere'])):
        df1.loc[i, 'Premiere'] = pdDf.loc[i, 'Premiere'].year
    a = df1.groupby(['Premiere'])['Runtime'].sum().to_frame('Sum of Runtime')
    x = a.index.tolist()
    z = a.values.tolist()
    y = []
    for i in range(len(z)):
        y.append(z[i][0])
    print("\nThe year that has the biggest sum of Runtime is", x[y.index(max(y))], "with", max(y), "counts.\n")
    fig = plt.figure(figsize=(10, 7))
    plt.bar(x, y)
    plt.show()
