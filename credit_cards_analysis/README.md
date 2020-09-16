# Predefinisani projekat 2 - Prvi projekat (credit_cards_analysis)

## Zadatak 
Dat je skup podataka (credit_card_data.csv), koji sadrži sumarizaciju ponašanja korisnika kreditnih kartica.  
Zadatak je da se grupišu korisnici koji imaju slično ponašanje i da se odredi optimalan broj grupa i da se svaka od njih opiše. 

Svaki korisnik je opisan sa 18 atributa:
* CUSTID : identifikacioni broj nosioca kreditne kartice (kategorička) 
* BALANCE : stanje na računu dostupno za kupovinu
* BALANCEFREQUENCY : koliko često se menja balans, vrednost između 0 i 1 (1 = često, 0 = retko)
* PURCHASES : ukupan iznos potrošen na kupovinu
* ONEOFFPURCHASES : iznos potrošen na kupovinu jednokratno
* INSTALLMENTSPURCHASES : iznos potrošen na kupovinu na rate
* CASHADVANCE : iznos koji je korisnik uplatio unapred
* PURCHASESFREQUENCY : koliko često korisnik kupuje, vrednost između 0 i 1 (1 = često, 0 = retko)
* ONEOFFPURCHASESFREQUENCY : koliko često kupuje jednokratno (1 = često, 0 = retko)
* PURCHASESINSTALLMENTSFREQUENCY : koliko često kupuje na rate (1 = često, 0 = retko)
* CASHADVANCEFREQUENCY : koliko se često uplaćuje novac unapred
* CASHADVANCETRX : broj transakcija sa uplaćenim novcem unapred
* PURCHASESTRX : broj transakcija koje su vezane za kupovinu
* CREDITLIMIT : limit na kreditnoj kartici
* PAYMENTS : ukupan iznos uplaćen na karticu
* MINIMUM_PAYMENTS : minimalan iznos koji je korisnik uplatio na karticu
* PRCFULLPAYMENT : procenat ukupnog iznosa koji korisnik treba da uplati na karticu
* TENURE : koliko još važe usluge kreditne kartice

## Korišćene tehnologije i biblioteke
* **python** v. 3.6
* **pandas** - biblioteka za manipulaciju podacima
* **scikit-learn** - biblioteka koja sadrži implementaciju velikog broja algoritama
* **matplotlib** - biblioteka za vizualizacija podataka

## Realizacija rešenja 

### K-means algoritam
U ovom projektu korišćen je K-means algoritam kako bi se grupisali korisnici koji imaju slično ponašanje.  
K-means je algoritama za nenadgledano klasterovanje podataka, odnosno ne-hijerarhijska metoda grupisanja sličnih podataka i često se koristi u tzv. eksplorativnoj analizi podataka, upravo kako bi se grupisali korisnici koji imaju slično ponašanje.  
Korišćena je implementacija ovog algoritma koja se nalazi u **scikit-learn** biblioteci i kao parametar je prosleđen broj 3, odnosno broj klastera ili grupa u koje svrstavamo korisnike biće 3.
```
# pokrecemo k means algoritam
# broj klastera je utvrdjen metodom lakta (elbowMethod.py)
km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df)

# dobijamo koordinate centara klastera
cl_centers = km.cluster_centers_
```
**Napomena:** K-means *nije* deterministički - pošto se centri inicijalizuju nasumično, ako ga pokrenemo više puta možemo dobiti različite rezultate. U slučaju ovog projekta npr. možemo dobijati različite ali približno iste srednje vrednosti po kolonama, ali one neće bitno uticati na karateristike grupa.

### Metoda lakta (elbow method)
Za određivanje optimalnog broja klastera korišćena je metoda lakta. Za određen broj K (klastera) se vrši klasterizacija i zatim se računa SSE (suma kvadratnih grešaka). SSE se računa tako što se unutar svakog klastera sumiraju kvadrati udaljenosti podataka od centra klastera, i zatim se sve to opet sumira. 
```
sse = []
k_rng = range(1, 10)
# racunamo sumu kvadratnih gresaka za svaki broj klastera iz k_rng
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df)
    sse.append(km.inertia_)
```
**Napomena:** Posmatrali smo 9 kolona iz priloženog csv fajla pa zato k_rng ide do 10.
Dalje smo sa grafika pročitali broj klastera (3) koje smo kasnije koristili u K-means algoritmu.

### Izostavljanje kolona
Prilikom grupisanja korisnika, izostavili smo pojedine kolone:
* CUSTID : pojedinačno obeležje korisnika nam ne znači u ovom slučaju
* BALANCEFREQUENCY : utvrdili smo da se svim grupama korisnika približno često menja balans pa smo izostavili ovu kolonu, jer se naspram nje ne razlikuju mnogo korisnici

  x| Grupa 1|Grupa 2|Grupa 3 
  -- | -------|-------|------  
  BALANCEFREQUENCY | 0.95 | 0.85 | 0.93  
  
* PURCHASES : ukupan iznos potrošen na kupovinu se može dobiti iz kolona ONEOFFPURCHASES i INSTALLMENTSPURCHASES
* PURCHASESFREQUENCY : koliko često korisnik kupuje možemo zaključiti iz kolona ONEOFFPURCHASESFREQUENCY i PURCHASESINSTALLMENTSFREQUENCY
* CASHADVANCEFREQUENCY : koliko se često uplaćuje novac unapred
* PURCHASESTRX : broj transakcija koje su vezane za kupovinu
* MINIMUM_PAYMENTS : minimalan iznos koji je korisnik uplatio na karticu možemo dobiti iz PAYMENTS
* PRCFULLPAYMENT : procenat ukupnog iznosa koji korisnik treba da uplati na karticu 
* TENURE : utvrdili smo da sve grupe korisnika imaju približno isti rok važenja kreditne kartice pa smo izostavili ovu kolonu, jer se naspram nje ne razlikuju mnogo korisnici

  x| Grupa 1|Grupa 2|Grupa 3 
  -- | -------|-------|------  
  TENURE | 11.83 | 11.44 | 11.54 

## Pokretanje projekta
1. Projekat otvorimo u *PyCharm* razvojnom okruženju.
1. Odgovarajuću skriptu pokrećemo desnim klikom miša na odgovarajući fajl, i zatim odaberemo opciju *Run 'imeFajla'*.  

Utvrđivanje broja klastera i iscrtavanje odgovarajućeg grafika se dobija pokretanjem *elbowMethod.py* fajla.  
Izvršavanje K-means algoritma, grupisanje korisnika, opisivanje tih grupa i iscrtavanje odgovarajućih grafika dobijamo pokretanjem *kMeans.py* fajla.  
**Napomena:** Proveriti koji je python interpreter podešen. Projekat se neće moći pokrenuti sa ranijim verzijama python interpretera (npr. *python 2.7*).
