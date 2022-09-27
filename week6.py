'''
Saat tässä tehtävässä koodin, jota käytettiin tunnilla suoran sovittamiseksi dataan
Sinun tehtävänäsi on sovittaa toisen asteen yhtälö f(x) = t2*x^2 + t1*x + t0 dataan, jonka 
muoto on paraabelin eli toisen asteen yhtälön muotoinen. Eli sinun pitää osata derivoida
kustannusfunktio t2, t1 ja t0 parametrien suhteen, jotta voit muodostaa luupin, jossa
kaikkien noiden parametrien derivaatat lasketaan tunnetuista datapisteistä.

Lisää tulostukseen myös t2 parametrien säätöarvot

Lisätehtävänä voit pohtia miten saat nopeutettua laskentaa. Annetussa koodissa käytetään
vielä pythonin listoja ja ne kannattanee korvata Numpyn arrayksi.

Ja toinen lisätehtävä on muuttaa plot komennot siten, että käytetään axes objekteja tuon
helpon matplotlib.pyplot sijasta ja vaikka niin, että yhteen kuvaan tulostetaan t0, t1 ja t2 säätökäyrät
eli kerätään nuo säätököyrät yhteen matriisiin ja printataan tuo matriisi.

'''

import matplotlib.pyplot as plt
import numpy as np

# lets make first random data to which we try to fit a
# straight line

M = 100 #datapoints
#x = np.linspace(50, 300,M) #start, stop, step
#y = x*1000 + 100000*np.random.random(M)

# Data toisen asteen polynomisovitusta varten
x = 5*np.random.randn(M)
y = x**2 + 5*np.random.randn(M)


# now let's try to fit a line to that known data
# our hypothesis function h(x) = t1*x + t0, where
# t1 and t0 are randomly initialized parameters
t0 = np.random.randn(1)
t1 = np.random.randn(1)
t2 = np.random.randn(1) 


# let's now iterate many times. I.e. each time
# we calculate a new gradient value for our cost function
# and we adjust your (originally random) t0 and t1 parameters
# towards hopefully right values
# and lets also collect adjusted t0 and t1 values
# to see how learning takes place.
t0_adjusted_values = []
t1_adjusted_values = []
t2_adjusted_values = []
rate = 0.00003   # this is learning rate parameter


plt.figure(1)
for rounds in range(100):
    grad_t0 = 0
    grad_t1 = 0
    grad_t2 = 0
    # lets calculate new gradient values for t0 and t1 based on
    # M known values
    #print(M)
    for i in range(M):
        # our cost function c = (1/2M)*(h(x)-y)^2
        # where M = number of known values
        # partial derivatives for t1 and t0 are
        # t0 =>(1/M)*(h(x)-y)*1 => (1/M)*((t1*x(i) + t0) - y(i)) * 1
        # t1 =>(1/M)*(h(x)-y)*x => (1/M)*((t1*x(i) + t0) - y(i)) * x(i)
        # where i goes from 1 => M
        grad_t0 = grad_t0 + ((t2*x[i]**2+t1*x[i] + t0) - y[i])
        grad_t1 = grad_t1 + ((t2*x[i]**2+t1*x[i] + t0) - y[i]) * x[i]
        grad_t2 = grad_t2 + ((t2*x[i]**2+t1*x[i] + t0) - y[i]) * x[i]**2


    # and now we can update parameters t0 and t1 with new gradient step
    t0 = t0 - (rate/(M*1.0))*grad_t0
    t1 = t1 - (rate/(M*1.0))*grad_t1
    t2 = t2 - (rate/(M*1.0))*grad_t2

    t0_adjusted_values.append(t0)
    t1_adjusted_values.append(t1)
    t2_adjusted_values.append(t2)


    # and finally lets visualize results
    xmin = np.min(x)
    xmax = np.max(x)
    x1 = np.linspace(xmin,xmax,100)
    h = t2*x1**2 + t1*x1 + t0


    plt.subplot(2,2,1)
    plt.plot(t0_adjusted_values,'-*b')
    plt.title('Adjusted t0 values')

    plt.subplot(2,2,2)
    plt.plot(t1_adjusted_values,'-*g')
    plt.title('Adjusted t1 values ')

    plt.subplot(2,2,3)
    plt.plot(t2_adjusted_values,'-*g')
    plt.title('Adjusted t2 values ')
    
    plt.subplot(2,2,4)
    #plt.clf()
    plt.plot(x,y,'.r')
    plt.plot(x1, h, '-b')
    plt.title('Known datapoints and fitting ^2 line')
    plt.pause(0.03)



#säätökäyrät matriisiin.
'''
s = (101, 3)
a = np.zeros(s)
a[0:-1, 0] = t0_adjusted_values
a[0:-1, 1] = t1_adjusted_values 
a[0:-1, 2] = t2_adjusted_values 
print(a)

plt.figure(2)
plt.plot(a)
'''
plt.show()





