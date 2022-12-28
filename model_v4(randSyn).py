from neuron import h
from neuron import gui
import matplotlib.pyplot as plt
import numpy as np
import json
import random

h.load_file("pyrCell.hoc")
myCell = h.pyrCell()

file_path = "./slice_apic[20]_rand_cluster.json"
with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)

seg_list=[f'seg{x}' for x in range(1,6)]
cluster_Obj = json_data



stim = h.NetStim()
stim.number=1
stim.start=5000
stim.interval=0

syns=[]
for seg in seg_list:
    rseg = random.randrange(0,len(cluster_Obj[seg])+1)
    print(rseg)
    s_val = cluster_Obj[seg][rseg]           #s_val[0] = dendrite num; s_val[1] = nseg num
    syn = h.Exp2Syn(s_val[1], sec=myCell.apic[s_val[0]])
    syn.e = 0
    syn.tau1 = 0.3
    syn.tau2 = 3
    syns.append(syn)

ncs=[]
for i in range(5):
    nc = h.NetCon(stim, syns[i])
    nc.delay+=30
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