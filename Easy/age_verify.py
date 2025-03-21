# ตรวจสอบอายุเข้าโรงหนัง
# ถ้าอายุ 18 ขึ้นไป ให้พิมพ์ "Allowed" ถ้าน้อยกว่าให้พิมพ์ "Not Allowed"
age = int(input("Enter your age: "))
if age >= 18:
    print("Allowed")
else:
    print("Not Allowed")