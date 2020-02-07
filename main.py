def getx0():
    while 1:
        try:
            return float(input("Input X0> "))
        except:
            print("Invalid Input")

def getnextx(xn, r):
    return r * xn * (1-xn)

def getr():
    while 1:
        try:
            return float(input("Input r> "))
        except:
            print("Invalid Input")

def getlist():
    x = [getx0()]
    r = getr()
    for i in range(50):
        print(i, x[-1])
        x.append(getnextx(x[-1], r))

def main():
    getlist()

if __name__ == "__main__":
    main()
