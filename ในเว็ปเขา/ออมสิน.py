oneB = int(input("The number of 1 baht coin = "))
twoB = int(input("The number of 2 baht coin = "))
fiveB = int(input("The number of 5 baht coin = "))
tenB = int(input("The number of 10 baht coin = "))

print("Total:")
total = oneB + (twoB*2) + (fiveB*5) + (tenB*10)
if total > 500:
    print(str(total*2) + " baht")
else:
    print(str(total) + " baht")