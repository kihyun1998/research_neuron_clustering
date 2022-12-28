from neuron import h
import json

h.load_file("pyrCell.hoc")
myCell = h.pyrCell()


#open json file
file_path = "./distance.json"
with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)
file_path2 = "./cluster3.json"
with open(file_path2, 'r') as json_file2:
    json_data2 = json.load(json_file2)
new_cluster = json_data2['res']


test_cluster = {}

for i in new_cluster:
    r=0;cnt=0;idx=[]
    for j in range(11):
        if 930 < json_data[f"apic[{i}]"][f'myCell.apic[{i}({r})]'] < 1000:
            cnt+=1
            idx.append([i,r])
        r+=0.09
        r=round(r,2)
    if cnt>=5:
        test_cluster[f'apic[{i}]'] = idx

file_path3 = "./test_cluster.json"
with open(file_path3, 'w') as outfile:
    json.dump(test_cluster, outfile, indent=4)