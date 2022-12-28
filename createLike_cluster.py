"""
Find and store dendrite intervals in a specific range
"""

from neuron import h
import json

h.load_file("pyrCell.hoc")
myCell = h.pyrCell()


#open json file
file_path = "./distance.json"
with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)
file_path2 = "./cluster.json"
with open(file_path2, 'r') as json_file2:
    json_data2 = json.load(json_file2)

key1 = ["n1","n2","n3","n4","n5"]


cut_start = 927
cut_end = 1001


test_cluster2 = []
for i in key1:
    for j in json_data2[i]:
        r=0;cnt=0;idx=[]
        for sec in range(12):
            if cut_start < json_data[f"apic[{j}]"][f'myCell.apic[{j}({r})]'] < cut_end:
                cnt+=1
                idx.append([j,r])
            r+=0.09
            r=round(r,2)
            
        if cnt>=5:
            test_cluster2.append(idx)


file_path3 = "./full_apic[20]_rand_cluster.json"
with open(file_path3, 'w') as outfile:
    json.dump(test_cluster2, outfile, indent=4)