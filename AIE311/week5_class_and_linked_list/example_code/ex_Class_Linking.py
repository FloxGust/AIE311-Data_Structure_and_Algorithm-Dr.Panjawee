class Box5():
    Box_name = ""
    Box_Colour = ""
    Box_width = ""
    Box_height = ""
    Box_length = ""
    def Value(self):
        print("Box name = " + str(self.Box_name.B_Name))
        print("Box colour = " + str(self.Box_Colour.B_Colour))
        print("Box width = " + str(self.Box_width.B_Width))
        print("Box height = " + str(self.Box_height.B_Height))
        print("Box length = " + str(self.Box_length.B_Length))

class Name():
    def __init__(self,input):
        self.B_Name = input
    
class Colour():
    B_Colour = ""
    
class Width():
    B_Width = ""
    
class Height():
    B_Height = ""
    
class Length():
    B_Length = ""
    
## Create object ##
FifthBox = Box5()
FifthBoxName = Name("5th Box")
BoxColour = Colour()
BoxWidth = Width()
BoxHeight = Height()
BoxLength = Length()
## Assign object value ##
BoxColour.B_Colour = "Red"
BoxWidth.B_Width = 2
BoxHeight.B_Height = 3
BoxLength.B_Length = 4
## Link value ##
FifthBox.Box_name = FifthBoxName
FifthBox.Box_Colour = BoxColour
FifthBox.Box_width = BoxWidth
FifthBox.Box_height = BoxHeight
FifthBox.Box_length = BoxLength
## Print value
print("## Print fifth box value ##")
FifthBox.Value()