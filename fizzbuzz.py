def plingplang(num) :

    string = ""

    if (num % 3 == 0 or num % 5 == 0 or num % 7 == 0 ):
        if num % 3 == 0 :
            string += "Pling "
        if num % 5 == 0 :
            string += "Plang "
        if num % 7 == 0 :
            string += "Plong"
        print(string)
    else:
        print(num)


if __name__ == '__main__' :

    i = 1
    while i < 100:
        plingplang(i)
        i += 1