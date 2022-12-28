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


n1=[];n2=[];n3=[];n4=[];n5=[]
for i,dic in json_data.items():
    for j in dic:
        if j[15:17]=="0)" and dic[j] // 200 ==1:
            text = i.replace("apic","")
            text = text.replace("[","")
            text = text.replace("]","")
            n1.append(text)
        elif j[15:17]=="0)" and dic[j] // 200 ==2:
            text = i.replace("apic","")
            text = text.replace("[","")
            text = text.replace("]","")
            n2.append(text)
        elif j[15:17]=="0)" and dic[j] // 200 ==3:
            text = i.replace("apic","")
            text = text.replace("[","")
            text = text.replace("]","")
            n3.append(text)
        elif j[15:17]=="0)" and dic[j] // 200 ==4:
            text = i.replace("apic","")
            text = text.replace("[","")
            text = text.replace("]","")
            n4.append(text)
        elif j[15:17]=="0)" and dic[j] // 200 ==5:
            text = i.replace("apic","")
            text = text.replace("[","")
            text = text.replace("]","")
            n5.append(text)

#===========

        
n1 = list(map(int,n1))
n2 = list(map(int,n2))
n3 = list(map(int,n3))
n4 = list(map(int,n4))
n5 = list(map(int,n5))

ns =[]
ns.append(n1)
ns.append(n2)
ns.append(n3)
ns.append(n4)
ns.append(n5)


file_path2 = "./cluster.json"
total2={}
for i,v in enumerate(ns):
    total2[f'n{i+1}'] = v

    with open(file_path2, 'w') as outfile:
        json.dump(total2, outfile, indent=4)