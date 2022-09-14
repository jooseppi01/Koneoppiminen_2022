from cmath import sin
from turtle import color, title
import numpy as np
import matplotlib.pyplot as plt
'''
Let's look in to matplotlib library properties and train ourselves
with Numpy array manipulations. Your tasks are the following:
1) Make 256*256 pixel picture (instructions given below). Current
   example plots RGB picture where Red component is all ones and G,B components are zero
   thus picture is all red. Your task is to modify picture in such a way that pixels
   at range 0-127 (rows), 0-127 (columns) show red picture area
   at range 0-127 (rows), 128-256 (columns) show green picture area
   at range 128-256 (row), 0-127 (columns) show blue picture area
   at range 128-256 (row), 128-256 (columns) show gray picture area 

'''

size = 256
kuva = np.zeros((size,size,3))
kuva[:,:,0]= np.ones((size,size))

kuva[0:127,128:256,0]= np.zeros((127,128))
kuva[0:127,128:256,1]= 1  #vihreä

kuva[128:256,0:127,0]= np.zeros((128,127))
kuva[128:256,0:127,2]= np.ones((128,127))

kuva[128:256,128:256,2]= 0.5
kuva[128:256,128:256,0]= 0.5
kuva[128:256,128:256,1]= 0.5

plt.imshow(kuva)
plt.show()


#Let's look at matplotlib library basic usage tutorials. There is an example
#how to create 3 figures as shown below

'''
fig1 = plt.figure()  # an empty figure with no Axes
fig2, ax = plt.subplots()  # a figure with a single Axes
fig3, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
plt.show()
'''

#creating 1, 2, 3 and 4 hz numpy arrays.

t = np.arange(0, 1, 0.01)
f1 = 1
f2 = 2
f3 = 3
f4 = 4
sini1 = np.sin(2*np.pi*f1*t)
sini2 = np.sin(2*np.pi*f2*t)
sini3 = np.sin(2*np.pi*f3*t)
sini4 = np.sin(2*np.pi*f4*t)


#printing them to plots.

fig1 = plt.figure(1)
plt.plot(sini1)
plt.title('sini 1hz')

fig2, ax = plt.subplots()
ax.plot(sini2)
ax.set_title('sini 2hz')

fig3, axs = plt.subplots(2, 2)
axs[0, 0].plot(sini1, color = ('y'), linestyle = ('dotted'))
axs[0, 0].set_title('1hz sini')

axs[0, 1].plot(sini2, color = ('red'))
axs[0, 1].set_title('2hz sini')

axs[1, 0].plot(sini3, color = ('blue'), linestyle = ('dashed'))
axs[1, 0].set_title('3hz sini')

axs[1, 1].plot(sini4, color = ('c'))
axs[1, 1].set_title('4hz sini')


#matrix where you have a 1 second 2 Hz sine signal and its second power.

s = (100, 3)
a = np.zeros(s)
a[0:-1, 0] = sini1[0:-1]

a[0:-1, 1] = sini2[0:-1] #-1 meinaa sitä että viimeiseen riviin/sarakkeeseen.

a[0:-1, 2] = sini4[0:-1] #2hz^2, eli 4hz.

plt.figure(4)
plt.title('1hz, 2hz and 2hz^2 sine waves')
plt.plot(a)
plt.show()


'''
Your tasks are the following:
1) create 4 NumPy arrays containing 1 second sine signals with 1, 2, 3, 4 Hz
    HINT:
    create first time t = np.arange(0,1,0.01), where t starts from 0, ends at 0.99
    and then use np.sin and np.pi functions to genereate certain sine signals with certain
    frequencies. And remember the equation = sin(2*pi*f*t)
2) print 1 Hz sine signal to fig1
3) print 2 Hz sine signal to fig2
4) print 1,2,3,4 Hz sine signals to fig3 subplots. HINT: remember that axs is 2*2 matrix. 
   thus accessing second subplot goes with axs[0,1], where 0 = first row, 1 = second column.
5) print titles to all 3 figures
6) change line type and color of line of all 4 subplots at fig3 

7) And finally as we hopefully saw during the lectures that one can put
   many signals to a matrix and then just print matrix and all columns are
   seen as separate signals. Make signal matrix where you have a 1 second 2 Hz sine
   signal and its second power. And print those to a same figure.

'''



