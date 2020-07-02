from sklearn.cluster import KMeans
import pandas as pd
from matplotlib import pyplot as plt

# CUST_ID,BALANCE,BALANCE_FREQUENCY,PURCHASES,ONEOFF_PURCHASES,INSTALLMENTS_PURCHASES,CASH_ADVANCE,PURCHASES_FREQUENCY,
# ONEOFF_PURCHASES_FREQUENCY,PURCHASES_INSTALLMENTS_FREQUENCY,CASH_ADVANCE_FREQUENCY,CASH_ADVANCE_TRX,PURCHASES_TRX,CREDIT_LIMIT,
# PAYMENTS,MINIMUM_PAYMENTS,PRC_FULL_PAYMENT,TENURE
#

df = pd.read_csv("../data/credit_card_data.csv")
# izostavljamo kolonu CUST_ID jer je necemo koristiti za racunanje
df.drop(columns=['CUST_ID', 'PURCHASES', 'PURCHASES_FREQUENCY', 'CASH_ADVANCE_FREQUENCY', 'PURCHASES_TRX',
                 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT', 'TENURE', 'BALANCE_FREQUENCY'], inplace=True)
df.dropna(inplace=True)

sse = []
k_rng = range(1, 10)
# racunamo sumu kvadratnih gresaka za svaki broj klastera iz k_rng
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df)
    sse.append(km.inertia_)

# podesavanje parametara grafika i njegovo iscrtavanje
plt.xlabel('Broj klastera (K)')
plt.ylabel('Suma kvadratnih gresaka (SSE)')
plt.plot(k_rng, sse, '-ok')
plt.grid(True)
plt.title(label='Odredjivanje broja klastera koristeci metodu lakta', loc='center')
plt.show()
