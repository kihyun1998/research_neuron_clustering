"""
test whole section distance/ max-min
"""

from neuron import h
from neuron import gui
import matplotlib.pyplot as plt
import numpy as np

h.load_file("pyrCell.hoc")
myCell = h.pyrCell()

stim = h.NetStim()
stim.number=1
stim.start= 5000
stim.interval=0

syn = h.Exp2Syn(0.18, sec=myCell.apic[20])
syn.e = 0
syn.tau1 = 0.3
syn.tau2 = 3

nc = h.NetCon(stim, syn)
nc.delay=1
nc.weight[0] = 0.001


t=h.Vector().record(h._ref_t)

recList=[]
rec_s = h.Vector().record(myCell.soma(0.5)._ref_v)

for i in range(11,76):
    rec = f'h.Vector().record(myCell.apic[{i}](0.5)._ref_v)'
    recList.append(rec)



h.finitialize(-60)
h.continuerun(5200)

import csv
import pandas as pd

with open("rec_soma.csv", "w") as f:
    csv.writer(f).writerows(zip(t, rec_s))

for i,v in enumerate(recList):
    with open(f"rec_{i}.csv", "w") as f:
        csv.writer(f).writerows(zip(t, v))


# plt.ylabel('Voltage [mV]')
# plt.xlabel('Time [ms]')
# plt.xlim(4975,5075)
# plt.plot(t,rec1,color='limegreen',label='soma(0.5)')
# plt.plot(t,rec2,color='violet',label='apic[11](0.5)')
# plt.plot(t,rec3,color='dodgerblue',label='apic[49](0.5)')
# plt.legend()
# plt.show()