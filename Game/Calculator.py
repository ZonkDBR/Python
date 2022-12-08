a = input("Masukkan angka! \n")
c = input("Masukkan Operator! \n")
b = input("Masukkan angka! \n")

def Operator() :
    try:
        if c == "+" :
            d = float(a) + float(b)
            print(d)
        elif c == "-" :
            d = float(a) + float(b)
            print(d)
        elif c == "*" :
            d = float(a) * float(b)
            print(d)
        elif c == "/" :
            d = float(a) / float(b)
            print(d)
        elif c == "%" :
            d = float(a) % float(b)
            print(d)
        elif c == "**" :
            d = float(a) ** float(b)
            print(d)
        elif c == "//" :
            d = float(a) // float(b)
            print(d)
        else:
            print("Invalid Operator!")
    except ValueError :
        print("Invalid input!")

Operator()

e = input("Keluar atau tidak? y or n \n")
while e != "y" :
    if e == "n" :
        a = input("Masukkan angka! \n")
        c = input("Masukkan Operator! \n")
        b = input("Masukkan angka! \n")
        Operator()
        e = input("Keluar atau tidak? y or n \n")
else:
    print("Selesai")