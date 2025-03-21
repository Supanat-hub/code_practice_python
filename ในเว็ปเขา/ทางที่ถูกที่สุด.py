p = int(input("The number of people = "))
d = float(input("Distance = "))

bus = max(5, d * 5) * p
if d <= 3:
    taxi_per_car = 35
else:
    taxi_per_car = 35 + (d - 3) * 2

num_cars = (p + 3) // 4
taxis = taxi_per_car * num_cars

if bus < taxis:
    print("The cheaper travelling is by:\nbus")
    print("Cost:\n{} baht".format(bus))
else:
    print("The cheaper travelling is by:\ntaxi")
    print("Cost:\n{} baht".format(taxis))