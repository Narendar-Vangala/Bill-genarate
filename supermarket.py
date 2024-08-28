from datetime import datetime

name=input("enter your name:")
#List items
lists='''
Rice    Rs 20/Kg
sugar   Rs 30/Kg
Paneer  Rs 100/kg
Oil     Rs 80/liter
Boost   Rs 90/each
colgate Rs 70/each
'''

#declaration
price=0
pricelist=[]
totalprice=0
finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice':20,
       'sugar':30,
       'paneer':100,
       'oil':80,
       'boost':90,
       'colgate':70}
option=int(input("for list of items prees 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:

        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys() :
            price=quantity*(items[item])
            pricelist.append((item, quantity, items, price))  
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
else:
       print("sorry you entered item is not available ")
inp=input("can i bill the items yes or no:")
if inp=='yes':
     pass
if finalamount!=0:
    print(25*"=","Narendar Supermarket",25*"=") 
    print(28*"","Bhongir")
    print("Name:",name,30*" ","Date:" ,datetime.now())
    print(75*"_") 
    print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price') 
    for i in range(len(pricelist)):
              print(i,8*' ', ilist[i],3*' ',qlist[i],8*" " ,plist[i])
    print(75*"_")
    print(50*" ", 'TotalAmount:','Rs',totalprice)
    print("gst amount",40*" ",'Rs',gst)
    print(75*"_")
    print(50*" ", 'finalamount:','Rs',finalamount)
    print(75*"_")
    print(20*" ", "Thanks For Visiting")
    print(75*"_")

     
