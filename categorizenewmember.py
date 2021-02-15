def openOrSenior(data):
    s="Senior"
    o="Open"
    total=[]
    for m in data:
        #print(m[0], m[1])
        if int(m[0]) >= 55 and int(m[1]) > 7:
            total.append(s)
        else:
            total.append(o)
    return total