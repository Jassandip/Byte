def compute_divisors(num):
    divisors =[]
    for i in range(1,num+1):
        if num % i == 0:
            divisors.append(i) 
        else:
            pass
    return divisors 

def sum_of_divisors(num):
    divisors = compute_divisors(num)
    sum = 0
    for i in divisors:
        sum += i 
    return(sum)

def divisor_count(num):
    return(len(compute_divisors(num)))

def get_totatives(num):
    totatives =[]
    if num >= 1:
        totatives.append(1)
    else:
        pass
    a = list(range(2,num))
    for i in range(2,num):
        for j in range(2,i):
            if i % j == 0:
                a.remove(i)
                break
            else:
                pass
    totatives = totatives + a 

    x = compute_divisors(num)

    for i in x:
        for j in totatives:
            if i == j:
                totatives.remove(j)
            else:
                pass                
    return(totatives)



def totient(num):
    pass

if __name__ == "__main__":
    a = int(input("Please type in a number "))

    print(get_totatives(a))
        


        

