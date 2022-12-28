"""
This model shows spikes at input of synapses in specific dendrites.
"""

from neuron import h
from neuron import gui
import matplotlib.pyplot as plt
import numpy as np

h.load_file("pyrCell.hoc")
myCell = h.pyrCell()


stim = h.NetStim()
stim.number=5
stim.start=5000
stim.interval=800


n1=0;r1=11
syns=[]
for i in range(r1+1):
    syn = h.Exp2Syn(n1, sec=myCell.apic[63])
    n1+= 1/r1
    n1=round(n1,2)
    syn.e = 0
    syn.tau1 = 0.3
    syn.tau2 = 3
    syns.append(syn)


ncs=[]
for i in range(r1+1):
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
plt.xlim(4500,8500)
plt.plot(t,rec,label='soma(0.5)')
plt.legend()
plt.show()