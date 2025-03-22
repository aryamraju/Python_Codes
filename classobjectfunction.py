class giftbox:
    Ht=0
    wdth=0
def __init__(self,Ht,wdth):
    self.Ht=Ht
    self.wdth=wdth
def assemble(self):
    print("Height is"+str(self.Ht))
    print("Weight is"+str(self.wdth))
g1=giftbox(20,30)
g1.assemble()