"""
This model shows spikes when entering synapses of dendrites
divided by distance.
"""


from neuron import h
from neuron import gui
import matplotlib.pyplot as plt
import numpy as np
import json

file_path2 = "./cluster.json"
with open(file_path2, 'r') as json_file2:
    json_data = json.load(json_file2)
    
n5 = json_data["n5"]

h.load_file("pyrCell.hoc")
myCell = h.pyrCell()


stim = h.NetStim()
stim.number=10
stim.start=5000
stim.interval=400



total_syns=[]
for i in n5:
    syns=[]
    num1=0;r1=11
    for j in range(r1+1):
        syn = h.Exp2Syn(num1, sec=myCell.apic[i])
        num1+= 1/r1
        num1=round(num1,2)
        syn.e = 0
        syn.tau1 = 0.3
        syn.tau2 = 3
        syns.append(syn)
    total_syns.append(syns)


total_ncs=[]
for i in range(len(n5)):
    ncs=[]
    for j in range(r1+1):
        nc = h.NetCon(stim, total_syns[i][j])
        nc.delay=1
        nc.weight[0] = 0.0003
        ncs.append(nc)
    total_ncs.append(ncs)


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