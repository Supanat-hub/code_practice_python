def commission(cake, sticky_rice, orange_juice):
    total = (cake*10) + (sticky_rice*20) + (orange_juice*15)
    commis = 0
    if cake > 20:
        commis += (cake*3)
    else:
        commis += (cake*2)
    if sticky_rice > 30:
        commis += (sticky_rice*7)
    else:
        commis += (sticky_rice*5)
    if orange_juice > 30:
        commis += (orange_juice*5)
    else:
        commis += (orange_juice*3)
    if total > 500:
        commis += (total*0.1)
    print("Gross sales:")
    print(str(total) + " baht")
    print("Commission:")
    print(str(commis) + " baht")

c = float(input("The number of pieces of cake = "))
s = float(input("The number of packs of sticky rice with chicken = "))
o = float(input("The number of bottles of orange juice = "))

commission(c, s, o)