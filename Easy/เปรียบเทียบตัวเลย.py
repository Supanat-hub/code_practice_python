# เปรียบเทียบตัวเลข
# รับเลขสองตัวแล้วบอกว่าตัวไหนมากกว่า
# ถ้าเท่ากันให้แสดงว่าเท่ากัน
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
if num1 > num2:
    print(f"{num1} is greater")
elif num1 < num2:
    print(f"{num2} is greater")
else:
    print("Equal")