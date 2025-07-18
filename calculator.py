def add(n,m):
    return n+m

def sub(n,m):
    return n-m

def multi(n,m):
    return n*m

def div(n,m):
    return n/m



while True:
    print("Calculator")
    num1 = int(input('Number 1:'))
    num2 = int(input('Number 2:'))
    print('1: ADD +')
    print('2: SUB -')
    print('3: MULTIPLY *')
    print('4: DIVISION /')
    print('5: EXIT')
    char = int(input('Enter the operation : '))
    

    if char == 1:
        print(add(num1,num2))
    elif char == 2:
        print(sub(num1,num2))
    elif char == 3:
        print(multi(num1,num2))
    elif char == 4:
        print(multi(num1,num2))
    elif char == 5:
        break
    else:
        print('invalid input')