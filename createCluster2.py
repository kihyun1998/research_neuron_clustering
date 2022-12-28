"""
클러스터링 구간 나누고 저장
"""

from neuron import h
import json

h.load_file("pyrCell.hoc")
myCell = h.pyrCell()


#open json file
file_path = "./distance.json"
with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)



#===========
#거리별 자르기


start_8=[]; start_9=[]
for i,dic in json_data.items():
    for j in dic:
        if j[15:17]=="0)" and dic[j] // 100 == 8:
            text = i.replace("apic","")
            text = text.replace("[","")
            text = text.replace("]","")
            start_8.append(text)
        elif j[15:17]=="0)" and dic[j] // 100 == 9:
            text = i.replace("apic","")
            text = text.replace("[","")
            text = text.replace("]","")
            start_9.append(text)

#===========

        
start_8 = list(map(int,start_8))
start_9 = list(map(int,start_9))


clusters =[]
clusters.append(start_8)
clusters.append(start_9)



file_path2 = "./cluster2.json"
total2={}
for i,v in enumerate(clusters):
    total2[f'start_{i+8}'] = v

    with open(file_path2, 'w') as outfile:
        json.dump(total2, outfile, indent=4)