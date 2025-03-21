x = int(input("The number of boxes = "))

rice = (38 / 15) * x * 2  
chicken = (70 / 15) * x  
basil = (20 / 15) * x * 0.2  
chili = (45 / 15) * x * 0.2  
garlic = (80 / 15) * x * 0.02  
egg = 3.5 * x  

cost = rice + chicken + basil + chili + garlic + egg
price_per_box = (cost * 1.3) / x  

print("Total cost:")
print("{} baht".format(cost))
print("To get profit 30%, price per box:")
print("{} baht".format(price_per_box))
