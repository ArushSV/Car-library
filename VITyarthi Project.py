import random as r

a = {
    "Name": "BMW M4",
    "Country": "Germany",
    "Horse Power": "510 HP",
    "Torque": "650 Nm",
    "Top Speed": "290 km/hr",
    "Engine Type": "3.0L M TwinPower Turbo Inline-6 Petrol Engine (S58)",
    "Weight": "1800 kg",
    "Price": "1.9 Cr"
}

b = {
    "Name": "BMW M3",
    "Country": "Germany",
    "Horse Power": "510 HP",
    "Torque": "650 Nm",
    "Top Speed": "290 km/hr",
    "Engine Type": "3.0L TwinPower Turbo Inline-6 Petrol Engine (S58)",
    "Weight": "1805 kg",
    "Price": "1.5 Cr"
}

c = {
    "Name": "Toyota Supra MK5",
    "Country": "Japan",
    "Horse Power": "382 HP",
    "Torque": "500 Nm",
    "Top Speed": "250 km/hr",
    "Engine Type": "3.0L Turbocharged Inline-6 Petrol Engine (B58)",
    "Weight": "1540 kg",
    "Price": "90 Lakh"
}

d = {
    "Name": "Toyota GR86",
    "Country": "Japan",
    "Horse Power": "228 HP",
    "Torque": "250 Nm",
    "Top Speed": "226 km/hr",
    "Engine Type": "2.4L Naturally Aspirated Boxer-4 Petrol Engine",
    "Weight": "1270 kg",
    "Price": "55 Lakh"
}

e = {
    "Name": "Lamborghini Revuelto",
    "Country": "Italy",
    "Horse Power": "1015 HP",
    "Torque": "725 Nm",
    "Top Speed": "350 km/hr",
    "Engine Type": "6.5L Naturally Aspirated V12 Hybrid Petrol Engine",
    "Weight": "1772 kg",
    "Price": "8.9 Cr"
}

f = {
    "Name": "Lamborghini Huracan",
    "Country": "Italy",
    "Horse Power": "631 HP",
    "Torque": "600 Nm",
    "Top Speed": "325 km/hr",
    "Engine Type": "5.2L Naturally Aspirated V10 Petrol Engine",
    "Weight": "1422 kg",
    "Price": "4 Cr"
}

g = {
    "Name": "Ferrari SF90 XX",
    "Country": "Italy",
    "Horse Power": "1016 HP",
    "Torque": "804 Nm",
    "Top Speed": "320 km/hr",
    "Engine Type": "4.0L Twin Turbo V8 Hybrid Petrol Engine",
    "Weight": "1560 kg",
    "Price": "7.5 Cr"
}

h = {
    "Name": "Ferrari LaFerrari",
    "Country": "Italy",
    "Horse Power": "950 HP",
    "Torque": "900 Nm",
    "Top Speed": "350 km/hr",
    "Engine Type": "6.3L Naturally Aspirated V12 Hybrid Petrol Engine",
    "Weight": "1255 kg",
    "Price": "25 Cr"
}

i = {
    "Name": "Nissan GT-R R35",
    "Country": "Japan",
    "Horse Power": "565 HP",
    "Torque": "633 Nm",
    "Top Speed": "315 km/hr",
    "Engine Type": "3.8L Twin Turbo V6 Petrol Engine (VR38DETT)",
    "Weight": "1752 kg",
    "Price": "2.5 Cr"
}

j = {
    "Name": "Mercedes AMG C63",
    "Country": "Germany",
    "Horse Power": "680 HP",
    "Torque": "1020 Nm",
    "Top Speed": "280 km/hr",
    "Engine Type": "2.0L Turbocharged 4-Cylinder Plug-in Hybrid Engine",
    "Weight": "2165 kg",
    "Price": "1.95 Cr"
}

k = {
    "Name": "Mercedes AMG GT",
    "Country": "Germany",
    "Horse Power": "585 HP",
    "Torque": "800 Nm",
    "Top Speed": "315 km/hr",
    "Engine Type": "4.0L Twin Turbo V8 Petrol Engine",
    "Weight": "1970 kg",
    "Price": "3 Cr"
}

l = {
    "Name": "Audi R8",
    "Country": "Germany",
    "Horse Power": "602 HP",
    "Torque": "560 Nm",
    "Top Speed": "331 km/hr",
    "Engine Type": "5.2L Naturally Aspirated V10 Petrol Engine",
    "Weight": "1595 kg",
    "Price": "2.3 Cr"
}

m = {
    "Name": "Audi e-tron GT",
    "Country": "Germany",
    "Horse Power": "590 HP",
    "Torque": "830 Nm",
    "Top Speed": "250 km/hr",
    "Engine Type": "Dual Motor Electric Powertrain",
    "Weight": "2350 kg",
    "Price": "1.8 Cr"
}

n = {
    "Name": "Ford GT",
    "Country": "USA",
    "Horse Power": "660 HP",
    "Torque": "746 Nm",
    "Top Speed": "348 km/hr",
    "Engine Type": "3.5L Twin Turbo V6 EcoBoost Petrol Engine",
    "Weight": "1360 kg",
    "Price": "4.5 Cr"
}

o = {
    "Name": "Ford Mustang",
    "Country": "USA",
    "Horse Power": "486 HP",
    "Torque": "567 Nm",
    "Top Speed": "250 km/hr",
    "Engine Type": "5.0L Naturally Aspirated V8 Petrol Engine (Coyote)",
    "Weight": "1800 kg",
    "Price": "80 Lakh"
}

cars=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]

def car_info():
    print("Enter the Sr. No. of the car you would like the info about")
    print("Enter -1 for a random car")
    print("Enter 0 to exit")
    while True:
        x=int(input("Enter your choice: "))
        print("\n")
        if x==0:
            break
        elif x==-1:
            n=r.randint(0,14)
            for j in cars[n].items():
                print(j[0]," - ",j[1])
        elif x in range(1,16):
            for j in cars[x-1].items():
                print(j[0]," - ",j[1])
        else:
            print("Invalid Input")
        print("\n")

def compare_cars():
    x=int(input("Enter first car: "))
    y=int(input("Enter second car: "))
    if x not in range(1,16) or y not in range(1,16):
        print("Invalid Input")
    else:
        p=list(cars[x-1].keys())
        q=list(cars[x-1].values())
        s=list(cars[y-1].values())
        for i in range(0,8):
            print(p[i]," - ",q[i]," - ",s[i])
        print("\n")

def fav_cars():
    print("Make a list of your Top 3 Cars")
    x=int(input("Enter number for your First Car: "))
    y=int(input("Enter number for your Second Car: "))
    z=int(input("Enter number for your Third Car: "))
    l=[x,y,z]
    if x not in range(1,16) or y not in range(1,16) or z not in range(1,16):
        print("Invalid Input")
    else:
        print("Your List:")
        print("\n")
        for i in range (0,3):
            print("Car ",i+1)
            for j in cars[l[i]-1].items():
                print(j[0]," - ",j[1])
            print("\n")

for i in range (1,16):
    print (i," - ",cars[i-1]["Name"])
print("\n")
    
while True:
    print("Enter 1 to get Car Information")
    print("Enter 2 to compare Two Cars")
    print("Enter 3 to make a List of Your Favourite Cars")
    print("Enter 0 to Exit the Program")
    n=int(input("Enter Your Choice: "))
    print("\n")
    if n==1:
        car_info()
    elif n==2:
        compare_cars()
    elif n==3:
        fav_cars()
    elif n==0:
        break
    else:
        print("Invalid Input")
print("Thank You")
