'''
Install scikit-learn module with pip install scikit-learn command.

Tehtävät:
1. Luetaan dataout.csv tiedosto pandas data frameksi siten, että tiedostosta luetaan vai
   sarakkeet xyz ja labels. Eli jätetään se indeksi sarake, joka koostuu 0,1,2 jonosta pois. 
   Käytä dataframen read_csv funktiota ja sieltä parametreja delimiter=, header=, usecols=

2. Poistetaan edellä luetusta dataframesta sen ensimmäinen rivi, jossa siis xyz ja labels tieto.
   Tämä siksi, että jäljelle jäänyttä 60,3 matriisia ja string saraketta käytetään eri algoritmien
   opettamiseen. Käytä dataframe iloc metodia

3. Seuraavaksi suodatetaan dataframesta pois sellaiset rivit, joissa x,y tai z arvo on suurempi
   kuin 1023, mikä on Arduinon analogia muuntimen maksimi lukema. Eli poistetaan virheelliset 
   mittaustulokset. Tulosta dataframe rivistä 40 eteenpäin (iloc käsky) ennen suodatusta ja 
   suodatuksen jälkeen, jotta varmistut siitä, että osa riveistä poistuu suodatuksen avulla
   Selvitä internetin avulla kuinka pandas dataframen sarakkeen arvoja voi suodattaa.

4. Seuraavaksi irroitetaan dataframesta labels tiedot left, right, up ja down tietoja
   kertova sarake (sen pitäisi olla neljäs sarake. Voit kokeilla esim print(df[4]) komennolla)
   Muutetaan sarakkeen tyyppi as_type komennolla 'category' tyypiksi ja luodaan dataframeen
   vielä viides sarake ja alustetaan sinne df[4].cat.codes funktion avulla numeeriset arvot
   left, rigth, up ja down arvoja vastaamaan.

5. Seuraavaksi "irroitetaan" dataframesta x,y,z sarakkeet ja muodostetaan niistä yksi 
   NumPy array, jossa on kolme saraketta ja N kpl rivejä. Tämä array = matriisi = data on sitten
   se, mitä käytetään eri mallien datana opettamiseen. Irroitetaan myös numpy arrayksi
   se viides sarake joka edellisessä vaiheessa saatiin tehtyä. Ja tätä käytetään opetuksessa
   kertomaan, mitä kukin data matriisin rivi edustaa = labels. Ja muutetaan molemmat irroitetut
   data ja labels int tyyppisiksi.

6. Ja nyt vihdoin data on käsitelty algoritmin opettamiseen sopivaksi. Jaetaan data vielä
   training ja test datasetteihin ja käytetään siihen sklearn kirjaston train_test_split luokkaa
   jonka voi importata komennolla from sklearn.model_selection import train_test_split. Tee
   sellainen jako, että datasta 20% jätetään testaukseen ja 80% datasta käytetään opetukseen.
   Netistä löytyy taas hyviä esimerkkejä, miten tämä tehtään: https://realpython.com/train-test-split-python-data/

7. Ja lopuksi testataan random forest ja K-means algoritmien toimivuutta. Eli opetetaan opetusdatalla
   x_train,y_train sekä random forest että K-means malli. Ja sen jälkeen testataan mallin tarkkuus
   x_test,y_test datalla. Ja ylimääräisenä tehtävänä voi vielä mitata kummastakin algoritmista kuinka
   kauaan mallin opettaminen kestää ja kuinka kauan yhden ennustuksen tekeminen mallilla kestää. Ja
   apuja löytyy taas netistä seuraavasti:
   K-means: https://towardsdatascience.com/knn-using-scikit-learn-c6bed765be75
   Random Forests:https://www.datacamp.com/tutorial/random-forests-classifier-python       
'''

import sklearn # This is anyway how package is imported
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv("dataout.csv",
delimiter ='\t',
header = None,                                   #ei lueta header riviä dataframeen.
usecols = [1, 2, 3, 4],                          #suodatetaan header sarake pois, aloittamalla 1.
names = ['x', 'y', 'z', 'labels'])

df2 = (df.iloc[1:-1])                            #poistetaan eka rivi dataframesta.

df2 = df2[df2['z'].astype(int)<1024]                     #pidetään sarakkeet joissa luku < 1024 
df2 = df2[df2['x'].astype(int)<1024]
df2 = df2[df2['y'].astype(int)<1024]

labels_to_category = df2['labels'].astype('category')

df2.insert(4, "newcol", labels_to_category)              #luodaan viides sarake.
df2['newcol'] = df2['newcol'].cat.codes                  #numeeriset arvot left, rigth, up ja down arvoja vastaamaan.

xyz = df2[['x', 'y', 'z']].astype(int).to_numpy()        #irroitetaan z,y ja z sarake ja muutetaan numpy arrayksi ja varmistetaan että tyyppi on int.
viides = df2['newcol'].astype(int).to_numpy()                        #sama tähän uuteen sarakkeeseen.


x = xyz                
y = viides
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)


#random forest
model = RandomForestClassifier(n_estimators = 4)
model.fit(x_train, y_train)
print('randomForest score: ', model.score(x_test, y_test))



#k-means
knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(x_train, y_train)
print('K-means score: ', knn.score(x_test, y_test))


