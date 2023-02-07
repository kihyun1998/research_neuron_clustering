from neuron import h
from neuron import gui
import matplotlib.pyplot as plt
import numpy as np

dis1=0.0
dis2=479.40492000490457
dis3=858.8415774267793

d1=abs(-60.0 - 35.91072077307407)
d2=abs(-60.0 - 7.675095348019124)
d3=abs(-60.0 - 5.891108890599301)
print(d1)

plt.ylabel('Voltage\'s Amplitude  [mV]')
plt.xlabel('distance to soma(0.5)')
plt.plot([dis1,dis2,dis3],[d1,d2,d3],color='limegreen',label='Amplitude change')
plt.legend()
plt.show()