def namelist(names):
    listofnames=''



    for i in range(len(names)):
       # print(n2[i]['name']s)

        listofnames+=str(names[i]['name'])
        if i == len(names)-2:
            listofnames+=str(' & ')
        else:
            listofnames+=str(', ')
    s=-2
    print(listofnames[:s])
