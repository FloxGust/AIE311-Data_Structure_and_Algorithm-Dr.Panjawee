## Class without initial function ##
class Box1():
    width = 1
    height = 1
    length = 1
    
## Print value ##
print(" ## Class without initial function ##")
FirstBox = Box1()
print("First box width = " + str(FirstBox.width))
FirstBox.width = 2
print("First box width = " + str(FirstBox.width))
print("#####################################")

## Class with initial function ##
class Box2():
    def __init__(self,width,height,length):
        self.width = width
        self.height = height
        self.length = length
        
## Print value ##
print(" ## Class with initial function ##")
SecondBox = Box2(1,1,1)
print("Second box width = " + str(SecondBox.width))
SecondBox.width = 2
print("Second box width = " + str(SecondBox.width))
print("##################################")

## Class without initial function + using function in class ##
class Box3():
    width = 1
    height = 1
    length = 1
    def calculate(self):
        self.Measure = self.width*self.height*self.length
        return self.Measure 
    
## Print value ##
print(" ## Class without initial function ##")
ThirdBox = Box3()
print("Third box width = " + str(ThirdBox.width))
print("Third box measure = " + str(ThirdBox.calculate()))
ThirdBox.width = 2
print("#After edited third box width#")
print("Third box width = " + str(ThirdBox.width))
print("Third box measure = " + str(ThirdBox.calculate()))
print("#####################################")

## Class with initial function + using function in class  ##
class Box4():
    def __init__(self,width,height,length):
        self.width = width
        self.height = height
        self.length = length
    def calculate(self):
        self.Measure = self.width*self.height*self.length
        return self.Measure 
        
## Print value ##
print(" ## Class with initial function ##")
FourthBox = Box4(1,1,1)
print("Fourth box width = " + str(FourthBox.width))
FourthBox.width = 2
print("Fourth box measure = " + str(FourthBox.calculate()))
print("#After edited third box width#")
print("Fourth box width = " + str(FourthBox.width))
print("Fourth box measure = " + str(FourthBox.calculate()))
print("##################################")