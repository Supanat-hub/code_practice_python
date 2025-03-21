# โรงภาพยนตร์แห่งหนึ่งสามารถกำหนดราคาของตั๋วได้เอง เดือนนี้เป็นช่วงเทศกาลภาพยนตร์ ราคาตั๋วจะลดลง 20% และพิเศษกว่านั้น ถ้าซื้อตั๋ว 3 ใบขึ้นไปราคาตั๋วจะลดลง 25%
cost = int(input("Enter ticket price: "))
num_of_tickets = int(input("Enter number of tickets: "))
total = cost * num_of_tickets
if num_of_tickets >= 3:
    total *= 0.75
else:
    total *= 0.8
print(str(total) + " baht")