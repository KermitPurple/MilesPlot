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

def getlist(x, r):
    lst = []
    for i in range(100):
        lst.append(x[-1])
        x.append(getnextx(x[-1], r))
    return lst

def round(num):
    roundednum = int(num)
    if num - roundednum >= 0.5:
        return roundednum + 1
    return roundednum

def graphlist(lst):
    scale = 30
    for i in range(scale, -1, -1):
        for lstitem in lst:
            if round(lstitem * scale) == i:
                print("*", end="")
            else:
                print(" ", end="")
        print()
         


def main():
    i = 0.001
    r = getr()
    while i < 1:
        print("\n",i)
        lst = getlist([i],r)
        graphlist(lst)
        i += 0.001

if __name__ == "__main__":
    main()
