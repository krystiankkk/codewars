def digital_root(n):
    sum=0
    sum1=0
    sum2=0
    for d in str(n):
        sum+=int(d)
    if sum >= 10:
        for di in str(sum):
            sum1+=int(di)
        if sum1>=10:
            for ds in str(sum1):
                sum2+=int(ds)
            return sum2
        else:
            return sum1
    else:
        return sum

print(digital_root(820))



print(digital_root(493193))