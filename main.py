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
    lst = []
    x = [getx0()]
    r = getr()
    for i in range(50):
        lst.append((i, x[-1]))
        x.append(getnextx(x[-1], r))
    return lst

def graphlist(lst):
    pass

def main():
    lst = getlist()
    graphlist(lst)

if __name__ == "__main__":
    main()
