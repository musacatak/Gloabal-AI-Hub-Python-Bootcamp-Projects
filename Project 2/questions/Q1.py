import pandas as pd
import matplotlib.pyplot as plt


def main():
    pdDf = pd.read_csv('NetflixOriginals.csv', encoding='latin-1')
    x = pdDf['Language'][pdDf['Runtime'] >= 40].value_counts(ascending=True)
    y = x.values.tolist()
    x = x.keys().tolist()

    y.append(0)
    x.append('Other Languages')
    i = 0
    while True:
        if i == len(y):
            break
        if y[i] < 4:
            y[len(y)-1] += y[i]
            del y[i]
            del x[i]
        else:
            i += 1
    plt.figure(figsize=(12.8, 7.2))
    expl = []
    c = 0.1
    for i in range(len(x)):
        if y[i] >= 1:
            expl.append(c)
            c += 0.001
        else:
            expl.append(0)

    plt.pie(y, labels=x, explode=expl)
    plt.legend(x, title="Languages")
    # show plot
    plt.show()
