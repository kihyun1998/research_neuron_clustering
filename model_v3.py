"""
This model shows spikes at the input of the synapses
 between the dendrites and synapses stored in the "test_cluster.json" file.
"""

from neuron import h
from neuron import gui
import matplotlib.pyplot as plt
import numpy as np
import json

file_path = "./test_cluster.json"
with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)
    
clusterD = json_data["apic[63]"]

h.load_file("pyrCell.hoc")
myCell = h.pyrCell()


stim = h.NetStim()
stim.number=10
stim.start=5000
stim.interval=0

syns=[]
num1=clusterD[0][1];r1=len(clusterD)
for i in range(r1):
    syn = h.Exp2Syn(num1, sec=myCell.apic[clusterD[0][0]])
    num1+= 0.09
    num1=round(num1,2)
    syn.e = 0
    syn.tau1 = 0.3
    syn.tau2 = 3
    syns.append(syn)

ncs=[]
for i in range(r1):
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