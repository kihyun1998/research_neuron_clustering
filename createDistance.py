

#모든 거리 확인 가능

from neuron import h
import json

h.load_file("pyrCell.hoc")
myCell = h.pyrCell()

file_path = "./distance.json"
total={}
for i in range(11,116):
    disLens = {};k=11
    x=0
    for j in range(k+1):
        disLen = h.distance(myCell.soma(0.5), myCell.apic[i](x))
        disLens[f'myCell.apic[{i}({x})]'] = disLen
        x += 1/k
        x=round(x,2)
    disLen = h.distance(myCell.soma(0.5), myCell.apic[i](1))
    disLens[f'myCell.apic[{i}({1})]'] = disLen
    total[f'apic[{i}]'] = disLens

    with open(file_path, 'w') as outfile:
        json.dump(total, outfile, indent=4)