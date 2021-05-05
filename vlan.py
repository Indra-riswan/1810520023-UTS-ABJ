
file=open("vlan-database.txt","a")
while True:
    x=input("input data VLAN baru y/n : ")
    print("="*35)
    if x=='y' or x=='Y':
        vlanID=input("Masukan VLAN ID : ")
        vlanName=input("Masukan VLAN Name : ")
        print("-"*35)
        file.write("VlanID :"+vlanID+"  "+"VlanName :"+vlanName+"\n")
    elif x=='n' or x=='N':
        file=open("vlan-database.txt","r")
        for item in file:
            item=item.strip()
            print(item)
        break
        
