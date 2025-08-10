rent=-int(input("Enter your hostel/flat rent ="))
food=int(input("Enter amount of food ordered ="))
electricity_spent=int(input("Enter total of electricity spend ="))
charge_per_unit=int(input("Enter the charge per unit ="))
persons=int(input("Enter number of persons living in hostel/flat ="))
total_bill=electricity_spent+charge_per_unit
output=(rent+food+total_bill)//persons
print("Each person will pay = ",output)