"""
Random synapse generation of interval distances such as apic[20].
"""

from neuron import h
import json

h.load_file("pyrCell.hoc")
myCell = h.pyrCell()

file_path = "./distance.json"
with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)

file_path2 = "./full_apic[20]_rand_cluster.json"
with open(file_path2, 'r') as json_file2:
    json_data2 = json.load(json_file2)

seg_interval = 14.6
cut_start = 927
cut_end = cut_start + seg_interval

rand_cluster = {}
for i in range(5):
    idx=[]
    for data in json_data2:
        for val in data:      #val[0]= dendrite; val[1]= seg
            if cut_start < json_data[f"apic[{val[0]}]"][f'myCell.apic[{val[0]}({val[1]})]'] < cut_end:
                idx.append(val)
    rand_cluster[f'seg{i+1}']=idx
    cut_start+=seg_interval
    cut_end+=seg_interval

file_path3 = "./slice_apic[20]_rand_cluster.json"
with open(file_path3, 'w') as outfile:
    json.dump(rand_cluster, outfile, indent=4)
