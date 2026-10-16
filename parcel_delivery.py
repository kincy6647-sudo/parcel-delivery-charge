name=input("Enter Customer Name: ")
weight=int(input("Enter Parcel Weight: "))
print("Place: ")
print("1.Local")
print("2.Inside-state")
print("3.Outside-state")
place=int(input())
print("Delivery Speed:")
print("1.Normal")
print("2.Fast")
speed=int(input())
if(weight<=0 or place<=0 or place>3 or speed<=0 or speed>2):
    print("Please Enter Correct Weight or Delivery Place or Delivery Speed")
elif(weight>20):
    print("Weight Not Allowed")
else:
    if(weight<=1):
        weight_amount=50
    elif(1<weight<=5):
        weight_amount=100
    else:
        total_weight=weight-5
        total_weight_amount=total_weight*20
        weight_amount=150+total_weight_amount
    if(place==1):
        place_charge=0
    elif(place==2):
        place_charge=40
    else:
        place_charge=100
    if(speed==1):
        speed_charge=0
    else:
        speed_charge=(weight_amount+place_charge)/2
    amount=weight_amount+place_charge+speed_charge
    if(amount>500):
        discount=amount/10
        total_amount=amount-discount
        print("Amount: "+str(total_amount))
    else:
        total_amount=amount
        print("Amount: "+str(total_amount))
    tax=total_amount*(18/100)
    print("Tax Amount: "+str(tax))
    tax_amount=total_amount+tax
    print("Total Amount: "+str(tax_amount))
