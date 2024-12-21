def Prime(Input, Count):
    Status = True
    if Count == Input:
        return True
    else:
        if Input % Count == 0:
            return False
        else:
            Count += 1
            Status = (Prime(Input, Count) and Status)
            return Status
        
def Recursive(Input):
    if Prime(Input, 2) == True:
        return ' is prime number'
    else:
        return ' is not prime number'
    
Input = 7
print(str(Input) + Recursive(Input))
Input = 9
print(str(Input) + Recursive(Input))