def Cumulative(Input):
    if Input == 0:
        return 0
    else:
        return Input + Cumulative(Input - 1)
    
print(Cumulative(5))