#Brian Onieal
#Question 3

#Discount calculator that shows total after subtracting the discount


package = float(99)
quantity = float(input("Please enter how many software packages you would like to purchase: "))
print(quantity)
print

if (quantity < 10):   #If the quantity is less than 10, no discount
    print("We're sorry, but the number of packages you have bought does not qualify you for a discount.")
    discount = 0
    print
    
elif quantity < 20:   #If the quantity is 10-19, 20% discount
    discount = float(0.2) *  quantity * package

elif quantity < 50:   #If the quantity is 20-49, 30% discount
    discount = float(0.3) *  quantity * package

elif quantity < 100:  #If the quantity is 50-99, 40% discount
    discount = float(0.4) *  quantity * package

elif quantity >= 100: #If the quantity is 100 or more, 50% discount
    discount = float(0.5) *  quantity * package
    
total = quantity * package - discount       #Calculation of the discount

#Discount totals
print("Your total discount for %d packages that you have puchased is %s" % (quantity,discount))
print
print("Your total for this purchase is %s" % (total))
