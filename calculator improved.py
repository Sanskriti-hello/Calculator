
def add():
    n1 = int(input("Enter Number 1: "))
    n2 = int(input("Enter Number 2: "))
    return n1 + n2

def subs():
    n1 = int(input("Enter Number 1: "))
    n2 = int(input("Enter Number 2: "))
    return n1 - n2

def mult():
    n1 = int(input("Enter Number 1: "))
    n2 = int(input("Enter Number 2: "))
    return n1 * n2

def div():
    n1 = int(input("Enter dividend: "))
    n2 = int(input("Enter divisor: "))
    if n2 == 0:
        return "Cannot divide by zero"
    return n1 / n2

def log(a):
    log_series=0.0
    temp=(a-1)/(a+1)
    for i in range(0,1000000):
        var=(temp**(2*i+1))/(2*i+1)
        log_series+=var
    return 2*log_series

def base_log():
    x=float(input("Enter the number: "))
    b=float(input("Enter the base: "))
    log_x=log(x)
    log_b=log(b)
    return log_x / log_b if log_b!=0 else print("Base is invalid!")

def factorial(n):
    pdt=1
    for i in range(1,n+1):
        pdt*=i
    return pdt

def trigo_sin():
    x=float(input("Angle in radian: "))
    while x>44/7:
        x = x % (44/7)
    sine_value = 0.0
    
    for n in range(0,40):
        fact=factorial(2*n+1)
        term = ((-1)**n) * (x**(2*n + 1)) / fact
        sine_value += term
    return sine_value

def trigo_cos():
    x=float(input("Angle in radian: "))
    while x>44/7:
        x = x % (44/7)
    cos_value = 0.0
    
    for n in range(0,40):
        fact=factorial(2*n)
        term = ((-1)**n) * (x**(2*n)) / fact
        cos_value += term
    return cos_value

def trigo_tan():
    sin = trigo_sin()
    cos = trigo_cos()
    if cos == 0:
        return "Not Defined!"
    return sin / cos

def trigo_cot():
    tan = trigo_tan()
    if tan == 0:
        return "Not Defined!"
    return 1 / tan

def trigo_cosec():
    sin = trigo_sin()
    if sin == 0:
        return "Not Defined!"
    return 1 / sin

def trigo_sec():
    cos = trigo_cos()
    if cos == 0:
        return "Not Defined!"
    return 1 / cos

def quadratic():
    a = int(input("Enter Coefficient of X^2: "))
    b = int(input("Enter Coefficient of X: "))
    c = int(input("Enter constant: "))
    Dis = b**2 - 4*a*c
    if Dis < 0:
        real = -b / (2*a)
        img = ((-Dis)**(0.5)) / (2*a)
        return f"Imaginary roots: {real} + {img}i, {real} - {img}i"
    else:
        root1 = (-b + ((-Dis)**(0.5)))/ (2*a)
        root2 = (-b - ((-Dis)**(0.5))) / (2*a)
        return (root1, root2) if root1 != root2 else root1

def user_input():
    while True:
        print("\nChoose an operation:")
        print("1 for sum")
        print("2 for difference")
        print("3 for product")
        print("4 for division")
        print("5 for logarithm")
        print("6 for sine")
        print("7 for cosine")
        print("8 for tangent")
        print("9 for cotangent")
        print("10 for cosecant")
        print("11 for secant")
        print("12 for quadratic equation")

        func_type = int(input("Enter your choice: "))
        result = None

        if func_type == 1:
            result = add()
        elif func_type == 2:
            result = subs()
        elif func_type == 3:
            result = mult()
        elif func_type == 4:
            result = div()
        elif func_type == 5:
            result = base_log()
        elif func_type == 6:
            result = trigo_sin()
        elif func_type == 7:
            result = trigo_cos()
        elif func_type == 8:
            result = trigo_tan()
        elif func_type == 9:
            result = trigo_cot()
        elif func_type == 10:
            result = trigo_cosec()
        elif func_type == 11:
            result = trigo_sec()
        elif func_type == 12:
            result = quadratic()
        else:
            print("Wrong Input. Try Again!")

        if result is not None:
            print("Result: ",result)

        choice = input("Wanna continue (y/n): ")
        if choice.lower() == "n":
            print("Thanks for using this!")
            break

user_input()
