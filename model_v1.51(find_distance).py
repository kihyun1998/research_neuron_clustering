"""
This model confirm input of synapses in specific dendrites ( one synapse ) 
ver. show distance
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
nc.weight[0] = 0.5


t=h.Vector().record(h._ref_t)

rec1 = h.Vector().record(myCell.soma(0.5)._ref_v)
rec2 = h.Vector().record(myCell.apic[11](0.5)._ref_v)
rec3 = h.Vector().record(myCell.apic[49](0.5)._ref_v)

dis1 = h.distance(myCell.soma(0.5),myCell.soma(0.5))
dis2 = h.distance(myCell.soma(0.5),myCell.apic[11](0.5))
dis3 = h.distance(myCell.soma(0.5),myCell.apic[49](0.5))
print(f"soma(0.5) = {dis1}\napic[11](0.5) = {dis2}\napic[49](0.5) = {dis3}")