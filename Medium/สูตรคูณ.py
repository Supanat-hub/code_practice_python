# แสดงแม่สูตรคูณของเลขที่รับมา

def table(n):
    for i in range(1, 13):
        print(f"{n} x {i} = {n*i}")

n = int(input("Enter number: "))
table(n)