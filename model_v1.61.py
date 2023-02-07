"""
This model confirm input of synapses in specific dendrites ( one synapse )weight = 0.0003
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

syn = h.Exp2Syn(0.45, sec=myCell.apic[33])
syn.e = 0
syn.tau1 = 0.3
syn.tau2 = 3

nc = h.NetCon(stim, syn)
nc.delay=1
nc.weight[0] = 0.0003


t=h.Vector().record(h._ref_t)

rec1 = h.Vector().record(myCell.apic[20](0.36)._ref_v)
rec2 = h.Vector().record(myCell.apic[63](0.18)._ref_v)


h.finitialize(-60)
h.continuerun(5200)


plt.ylabel('Voltage [mV]')
plt.xlabel('Time [ms]')
plt.xlim(4975,5075)
plt.plot(t,rec1,color='limegreen',label='apic[20](0.36)')
plt.plot(t,rec2,color='violet',label='apic[63](0.18)')
plt.legend()
plt.show()