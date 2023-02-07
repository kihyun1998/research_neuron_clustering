"""
This model confirm input of synapses in specific dendrites ( one synapse ) and multi plot
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
nc.weight[0] = 0.0003


t=h.Vector()
t.record(h._ref_t)

rec1 = h.Vector()
rec1.record(myCell.soma(0.5)._ref_v)
rec2 = h.Vector()
rec2.record(myCell.apic[11](0.5)._ref_v)
rec3 = h.Vector()
rec3.record(myCell.apic[49](0.5)._ref_v)



h.finitialize(-60)
h.continuerun(5200)


plt.ylabel('Voltage [mV]')
plt.xlabel('Time [ms]')
# plt.xlim(4900,5100)
plt.plot(t,rec1,color='limegreen',label='soma(0.5)')
plt.plot(t,rec2,color='violet',label='apic[11](0.5)')
plt.plot(t,rec3,color='dodgerblue',label='apic[49](0.5)')
plt.legend()
plt.show()