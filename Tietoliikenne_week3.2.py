import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft

taajuustaso = np.zeros((128),dtype=complex)
taajuustaso[3] = complex(1,1); # Tässä on nyt moduloitu yksi alikantoaalto

#moduloidaan alikantoaallot 10 ja 30.
taajuustaso[10] = complex(1,1);
taajuustaso[30] = complex(0,1);

# Moduloi tähän myös alikantoaallot 10 ja 30 QPSK-modulaatiota käyttäen
# Eli tarkoittaa siis sitä, että sinulla on käytettävissäsi 00 => 1+j, 11 => -1-j, 01 => -1+j ja 
# 10 => 1-j vaihtoehdot.

aikataso = ifft(taajuustaso[:]);

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(aikataso.real)
plt.title('Moduloidun signaalin kosinihaara')
plt.subplot(2,1,2)
plt.plot(aikataso.imag)
plt.title('Moduloidun signaalin sinihaara')

#muutetaan taajuustasoon
fourier_kos = fft(aikataso.real)
fourier_sin = fft(aikataso.imag)


plt.figure(2)
plt.subplot(2,1,1)
plt.plot(fourier_kos)
plt.title('fourier kosinihaara')
plt.subplot(2,1,2)
plt.plot(fourier_sin)
plt.title('fourier sinihaara')
plt.show()

#miten nuo bittipääätokset pitäisi saada????

# Ja tänne pitäisi opiskelijan sitten osata tehdä bittipäätökset
# Eli sinun pitää tulla aikatason signaalista takaisin taajuustasoon 
# ja tehdä bittipäätökset alikantoaaltojen 3, 10, 30 osalta.  


