# Predefinisani projekat 2 - Drugi projekat (cnn_project)

## Zadatak 
Dat je skup podataka koji sadrzi rendgenske slike pluca.  
Zadatak je da se klasifikuju snimci u tri grupe: Normal, Virus i Bacteria. Slike vezane za pusenje se mogu odbaciti jer postoje samo dva primera.   
Za ovu klasifikaciju se preporucuje upotreba konvolutivnih neuronskih mreza i ocekuje se isprobavanje vise razlicitih arhitektura mreze,
primena nekog vida regularizacije i opis kako je sve to uticalo na metrike koriscene za evaluaciju rada mreze.

## Korišćene tehnologije i biblioteke
* **python** v. 3.6
* **pandas** - biblioteka za manipulaciju podacima
* **TensorFlow** - biblioteka za numericka izracunavanja koja cini masinsko ucenje brzim i laksim
* **Keras** - biblioteka za rad sa neuronskim mrezama (u pozadini koristi *TensorFlow*) 

## Realizacija rešenja 

Dati problem smo resili upotrebom konvolutivnih neuronskih mreza.

### Fajl sortImgs.py

Fajl *sortImgs.py* sluzi za raspakivanje zip arhiva koje sadrze skup podataka za treniranje, validaciju i testiranje neuronske mreze.
Za razvrstavanje koristimo csv datoteke iz arhiva pomocu kojih razvrstavamo fajlove u 3 seta: train_set, valid_set i test_set, a svaki set ima 
3 grupe: normal, bacteria i virus.  
Na pocetku fajla se nalaze putanje do direktorijuma i konstanta *split_percent* koja odredjuje odnos izmedju kolicine podataka koja se koristi za treniranje i 
validaciju podataka. U ovom slucaju odnos je 70% : 30% (podaci za treniranje : podaci za validaciju).

```
path = "../data/chest_xray_data_set/"
path_test_zip = "../data/chest-xray-dataset-test/test/"
test_path = "../data/test_set/"
valid_path = "../data/valid_set/"
train_path = "../data/train_set/"
split_percent = 0.3
```

### Fajl main.py

Fajl *main.py* na pocetku sadrzi sledece konstante i putanje:

```
IMG_W, IMG_H = 64, 64  # sirina i visina slike
NUM_OF_CLASSES = 3  # broj klasa: normal, bacteria, virus
BATCH_SIZE = 32  # koliko se uzoraka uzima tokom jedne iteracije
EPOCHS = 30  # broj epoha

train_dir = "../data/train_set"
valid_dir = "../data/valid_set"
test_dir = "../data/test_set"
save_path = "../data/saved_models"
```

Takodje, u ovom fajlu se nalazi kod za pravljenje modela konvulutivne neuronske mreze:
```
model = Sequential()
model.add(Conv2D(64, kernel_size=(3, 3), input_shape=(IMG_W, IMG_H, 3)))
model.add(Activation("relu"))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))

.
.
.

model.add(Dense(NUM_OF_CLASSES, activation="softmax"))

model.summary()
```

Trenirani model testiramo na sledeci nacin:
```
tested = model.evaluate(test_generator)
```

## Pokretanje projekta
1. Projekat otvorimo u *PyCharm* razvojnom okruženju.
1. Smestimo zip fajlove, koji sadrze skup podataka, u *data* folder.
1. Odgovarajuću skriptu pokrećemo desnim klikom miša na odgovarajući fajl, i zatim odaberemo opciju *Run 'imeFajla'*.  
1. Pokrenemo skriptu *sortImgs.py*, koja ce raspakovati zipovane fajlove i sortirati slike u odgovarajuce foldere (test_set, train_set, valid_set).
1. Nakon toga mozemo pokrenuti treniranje i testiranje modela pokretanjem skripte *main.py*.

Skup podataka za ucenje i validaciju neuronske mreze mozete preuzeti [ovde](https://drive.google.com/file/d/1EoKNe24GDssnVjbps6wLWqMP2eODMqSg/view "chest_xray_data_set.zip")
a za testiranje [ovde](https://drive.google.com/file/d/1amr0Bn3ESNUeIcLkjLOV4KcgfBNRts3Q/view "chest-xray-dataset-test.zip").  

Detaljnije informacije o arhitekturama modela neuronskih mreza i rezultatima treniranja mozete pronaci u *data/models_description* folderu, 
a istrenirani modeli se nalaze u *data/saved_models* folderu.  

**Napomena:** Proveriti koji je python interpreter podešen. Projekat se neće moći pokrenuti sa ranijim verzijama python interpretera (npr. *python 2.7*).
