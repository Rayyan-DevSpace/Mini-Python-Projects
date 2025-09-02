# Inputs we need for calculator 
#  total rent
# total spending on snacks 
# electricity units spend
# charge per unit
# no of persons in room or flat

# Output
# Total amount per person should pay
person = int(input("Enter the no of persons in room/flat: "))
rent = int(input("Enter the hostel/flat rent: "))
food = int(input("Enter the amount spent on food ordered: "))
electricity_units = int(input("Enter the elctricity units used: "))
charge_per_unit = int(input("Enter the charge per unit: "))

total_electric_bill = electricity_units * charge_per_unit

output = (rent + food + total_electric_bill)//person

print("Bill per person is: ", output)