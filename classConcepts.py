class GiftBox :
    Ht=0       #height of the square
    Wdth=0     #width of the sqaure
g1=GiftBox()
g1.Ht=20
g1.Wdth=30

print(f"g1-> Ht={g1.Ht} , Wdth={g1.Wdth}")

g2=GiftBox()
g2.Ht=200
g2.Wdth=300

print(f"g2-> Ht={g2.Ht} , Wdth={g2.Wdth}")
g3=GiftBox()
g3=g1
g1=g2

print(f"g1-> Ht={g1.Ht} , Wdth={g1.Wdth}")
print(f"g2-> Ht={g2.Ht} , Wdth={g2.Wdth}")
print(f"g3-> Ht={g3.Ht} , Wdth={g3.Wdth}")