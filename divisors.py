def divisors(n):
    listofd=[]
    for i in range(2, n):
        if n % i ==0:
            listofd.append(i)
    #print(listofd)
    if len(listofd)==0:
        print('Primary')
    else:
        print(listofd)
divisors(253)
divisors(24)
divisors(25)
divisors(13)


#2 5 10 1