# นับจำนวนตัวอักษรสระในคำที่ป้อนเข้าไป
# สระ คือ a e i o u
text = input("Enter text: ")
count = 0
for c in text:
    if c in "aeiou":
        count += 1
print(count)