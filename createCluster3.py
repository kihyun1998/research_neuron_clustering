from neuron import h
import json

#open json file
file_path = "./distance.json"
with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)


h.load_file("pyrCell.hoc")
myCell = h.pyrCell()


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

new_cluster = []
with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)
    
for i in start_8:
    if json_data[f"apic[{i}]"][f'myCell.apic[{i}(0.99)]'] > 1000:
        new_cluster.append(i)
    
for i in start_9:
    if json_data[f"apic[{i}]"][f'myCell.apic[{i}(0.99)]'] > 1000:
        new_cluster.append(i)
res_cluster={}
new_cluster.sort()
file_path3 = "./cluster3.json"
res_cluster["res"]=new_cluster
with open(file_path3, 'w') as outfile:
    json.dump(res_cluster, outfile, indent=4)