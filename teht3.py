import numpy as np
import matplotlib.pyplot as plt

class signalAnalyser:
    def __init__(self,Fs,t):
        print('Constructor of signalAnalyser')
        self.fs = Fs
        self.Ts = 1/Fs
        self.t = t
        self.xakseli = np.arange(0,t,self.Ts)       # Aloitetaan nollasta, lopetaan t:n arvoon. self.ts kertoo välin suuruuden. 
        self.pituus = int(self.xakseli.size)        # Lasketaan kuinka monta alkiota self.xakseli sisältää.
        self.yakseli = np.zeros((1,self.pituus))    # luo arrayn jossa 1 rivi ja self.pituus verran nollia
      
        

    def create(self,f):
        pii = np.pi
        t = self.xakseli
        self.cosin = np.cos( 2 * pii * f * t) 
        self.sini = np.sin( 2 * pii * f * t)

    def plot(self,start,stop):
        plt.figure(1)
        plt.subplot(211) 
        plt.plot(self.xakseli[start:stop],self.cosin[start:stop],'-*')
        plt.title("$COS$")
        plt.subplot(212)
        plt.plot(self.xakseli[start:stop],self.sini[start:stop],'-*')
        plt.title("$SIN$")
        plt.show()
        

if __name__ == '__main__':
    obj = signalAnalyser(100, 2)  # luodaan objekti, jonka konstruktorille Fs = 100 Hz ja t = 2s
    obj.create(2)                # käytetään objektin create funktiota, missä f = 2 Hz
    obj.plot(0,100)               # käytetään objektin plot funktiota, plotataan väli 0 - 100 näytettä.
