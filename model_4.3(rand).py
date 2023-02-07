from neuron import h
from neuron import gui
import matplotlib.pyplot as plt
import numpy as np
import json
import random

h.load_file("pyrCell.hoc")
myCell = h.pyrCell()

file_path = "./slice_apic[20]_rand_cluster(ver. 10).json"
with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)

seg_list=[f'seg{x}' for x in range(1,3)]
cluster_Obj = json_data

startTime=5000
stims=[]
for i in range(5):
    stim = h.NetStim()
    stim.number=1
    stim.start=startTime
    stim.interval=0
    stims.append(stim)
    startTime+=0

syns=[]
for seg in seg_list:
    rseg = random.randrange(0,len(cluster_Obj[seg]))
    #s_val[0] = dendrite num; s_val[1] = nseg num
    s_val = cluster_Obj[seg][rseg]           
    syn = h.Exp2Syn(s_val[1], sec=myCell.apic[s_val[0]])
    print(s_val[0],s_val[1])
    syn.e = 0
    syn.tau1 = 0.3
    syn.tau2 = 3
    syns.append(syn)

ncs=[]
for i in range(2):
    nc = h.NetCon(stims[i], syns[i])
    nc.delay=0
    nc.weight[0] = 0.0003
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