from neuron import h
from neuron import gui
import matplotlib.pyplot as plt
import numpy as np
import json
import random

h.load_file("pyrCell.hoc")
myCell = h.pyrCell()


stim = h.NetStim()
stim.number=1
stim.start=5000
stim.interval=0

syns=[];seg=0.18
for i in range(5):
    syn = h.Exp2Syn(seg, sec=myCell.apic[20])
    seg+=0.18
    syn.e = 0
    syn.tau1 = 0.3
    syn.tau2 = 3
    syns.append(syn)

ncs=[]
for i in range(5):
    nc = h.NetCon(stim, syns[i])
    nc.delay=1
    nc.weight[0] = 0.0003
    ncs.append(nc)

t=h.Vector()
t.record(h._ref_t)

rec = h.Vector()
rec.record(myCell.soma(0.5)._ref_v)

h.finitialize(-60)
h.continuerun(10000)


plt.ylabel('Voltage [mV]')
plt.xlabel('Time [ms]')
plt.xlim(4900,5200)
plt.plot(t,rec,label='soma(0.5)')
plt.legend()
plt.show()