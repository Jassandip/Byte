def remove_duplicate(string):
    a = list(string) 
    b = []
    c = []
   
    for i in range(len(a)):
        if i == (len(a) - 1):
            c.append(a[i])
        elif a[i] == a[i + 1]:
            b.append(a[i])
        else:
            c.append(a[i])

    print("".join(c),"".join(b))
    

if __name__ == "__main__":
    print(remove_duplicate("balloonss"))
    print(remove_duplicate("aabbccddeded"))
    print(remove_duplicate("flabby aapples"))
