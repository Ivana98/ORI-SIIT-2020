import warnings

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from src.groupDescription import count, describe_groups

warnings.filterwarnings("ignore")

df = pd.read_csv("../data/credit_card_data.csv")

# izostavljamo kolone koje necemo koristiti za racunanje
df.drop(columns=['CUST_ID', 'PURCHASES', 'PURCHASES_FREQUENCY', 'CASH_ADVANCE_FREQUENCY', 'PURCHASES_TRX',
                 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT', 'TENURE', 'BALANCE_FREQUENCY'], inplace=True)
df.dropna(inplace=True)
originalDf = df.copy(deep=True)

# skaliranje podataka
df = StandardScaler().fit_transform(df)

# pokrecemo k means algoritam
# broj klastera je utvrdjen metodom lakta (elbowMethod.py)
km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df)

# dobijamo koordinate centara klastera
cl_centers = km.cluster_centers_

# transformisemo podatke da bismo mogli da ih prikazemo u 2D prostoru
pca = PCA(n_components=2)
transformedData = pca.fit_transform(df)
scaledDf = pd.DataFrame(data=transformedData, columns=['x_axis', 'y_axis'])

# dodajemo novu kolonu - broj klastera kojem korisnik pripada (grupa korisnika)
convert_ypred = pd.DataFrame({'CLUSTER': y_predicted[:]})
finalDf = pd.concat([scaledDf, convert_ypred], axis=1)
originalDf = pd.concat([originalDf, convert_ypred], axis=1)
originalDf.dropna(inplace=True)

# pozivaju se funkcije za racunanje srednje vrednosti za svaku kolonu i iscrtavanje 2 group bar plot-a
# i ispis opisa grupe
count(originalDf)
describe_groups(originalDf)

# prikaz podataka u 2D prostoru
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('x osa', fontsize=15)
ax.set_ylabel('y osa', fontsize=15)
ax.set_title('Grupe korisnika', fontsize=20)

clusters = [0, 1, 2]
colors = ['r', 'g', 'b']
markers = ['*', 'X', 'o']

legend = ['Grupa 1', 'Grupa 2', 'Grupa 3',
          'Centar grupe 1', 'Centar grupe 2', 'Centar grupe 3']

for target, color in zip(clusters, colors):
    f = finalDf.loc[finalDf['CLUSTER'] == target]
    ax.scatter(f['x_axis'], f['y_axis'], c=color, s=50)

for target, mark in zip(clusters, markers):
    ax.scatter(cl_centers[target, 0], cl_centers[target, 1], color='black', marker=mark, label='centroid')

ax.legend(legend)
ax.grid()
plt.show()
