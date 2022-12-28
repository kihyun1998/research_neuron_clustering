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


n1 = [];n2=[];n3=[];n4=[];n5=[]
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

        
n1 = map(int,n1)
n2 = map(int,n2)
n3 = map(int,n3)
n4 = map(int,n4)
n5 = map(int,n5)


#===========
#show shape
#===========


sec1=h.SectionList()
for i in n1:
    sec1.append(myCell.apic[i])
print(sec1)

stim = h.NetStim()
stim.number=5
stim.start=5000
stim.interval=200


num1=0;r1=11
syns=[]
for i in range(r1+1):
    syn = h.Exp2Syn(num1, sec=myCell.apic[31])
    num1+= 1/r1
    num1=round(num1,2)
    syn.e = 0
    syn.tau1 = 0.3
    syn.tau2 = 3
    syns.append(syn)

a=h.Shape(1)
a.color_list(sec1,2)
