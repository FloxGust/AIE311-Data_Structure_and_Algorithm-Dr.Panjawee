def Factorial(FactorialCount):
    if FactorialCount == 0:
        return 1
    else:
        return FactorialCount*Factorial(FactorialCount -1)
        
def main():
    number = 4
    res = Factorial(number)
    print(res)

if __name__ == '__main__':
    main()