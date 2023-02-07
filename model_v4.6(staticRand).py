from neuron import h
from neuron import gui
import matplotlib.pyplot as plt
import numpy as np
import json
import random

h.load_file("pyrCell.hoc")
myCell = h.pyrCell()

s_val=[[55, 0.36],[25, 0.09],[16, 0.36],
       [63, 0.18],[33, 0.54],[28, 0.45],
       [27, 0.18],[60, 0.63],[31, 0.36],[50,0.72]]


startTime=5000
stims=[]
for i in range(10):
    stim = h.NetStim()
    stim.number=1
    stim.start=startTime
    stim.interval=0
    stims.append(stim)
    startTime+=0

syns=[]
for i in range(10):         
    syn = h.Exp2Syn(s_val[i][1], sec=myCell.apic[s_val[i][0]])
    syn.e = 0
    syn.tau1 = 0.3
    syn.tau2 = 3
    syns.append(syn)

ncs=[]
for i in range(10):
    nc = h.NetCon(stims[i], syns[i])
    nc.delay=0
    nc.weight[0] = 0.1
    ncs.append(nc)

t=h.Vector()
t.record(h._ref_t)

rec = h.Vector()
rec.record(myCell.soma(0.5)._ref_v)

h.finitialize(-60)
h.continuerun(5200)


plt.ylabel('Voltage [mV]')
plt.xlabel('Time [ms]')
plt.xlim(4900,5100)
plt.plot(t,rec,label='soma(0.5)')
plt.legend()
plt.show()