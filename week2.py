import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

""" 
Tehtävä 1: 
- lataa Latest https://covidtracking.com/data/download/national-history.csv
  tiedosto pandas kirjaston avulla Pandas dataframeksi. 
- "Irroita" siitä ladattaessa'date','deaths','hospitalInc','hospitalNow' sarakkeet
- Piirrä matplotlib.pyplot kirjaston ja plt.subplot, plt.plot, plt.title, plt.show 
  komentojen avulla kuva, josta nähdään kuolleiden lukumäärät, sairaalapotilaiden
  inkrementaalinen kasvu ja kuinka paljon sairaalassa on potilaita eri päivinä.
- Selvitä minä päivänä potilaiden kasvu on ollut suurinta ja mikä on tuon päivän potilasmäärä

Tehtävä 2:
- Muuta kaikki dataFramen sarakkeet numpy arrayksi to_numpy() funktion avulla
- Tulosta kuolleiden määrä ja sairaalassa olleiden lukumäärät oikeassa järjestyksessä
  (huom päivämäärät ovat tiedostossa viimeisin päivämäärä ensin. Eli käännä tulostusjärjestys
   siten, että kuvaan tulostetaan deaths sarakkeen viimeisin alkio ensin jne.)
""" 

df = pd.read_csv("national-history (1).csv")

subset1 = (df["death"])
subset2 = (df["hospitalizedIncrease"])
subset3 = (df["hospitalizedCurrently"])
subset4 = (df["date"])

#tulostetaan minä päivänä potilaiden kasvu on ollut suurinta ja mikä on tuon päivän potilasmäärä
print(subset4[subset2.idxmax()])
print (int(subset3[subset2.idxmax()]))


plt.figure(1)
plt.subplot(311)
plt.plot(subset1)
plt.title("Deaths")

plt.subplot(312)
plt.plot(subset2)
plt.title("HospitalizedInc")

plt.subplot(313)
plt.plot(subset3)
plt.title("HospitalizedNow")

#-------------------------------------------------------------------
#tehdään uusi figure, käänteisenä

käänteinen1 = subset1.to_numpy()
käänteinen2 = subset2.to_numpy()
käänteinen3 = subset3.to_numpy()

plt.figure(2)
plt.subplot(311)
plt.plot(käänteinen1[::-1])
plt.title("Deaths")

plt.subplot(312)
plt.plot(käänteinen2[::-1])
plt.title("HospitalizedInc")

plt.subplot(313)
plt.plot(käänteinen3[::-1])
plt.title("HospitalizedNow")

plt.show()

