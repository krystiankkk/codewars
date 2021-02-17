def find_it(seq):
    hash_table={}
    for val in seq:
        if val in hash_table:
            hash_table[val]+=1
        else:
            hash_table[val]=1

    for vals in hash_table:
        if hash_table[vals] %2!=0:
            res=vals
    return res

find_it([1,1,1,1,1,1,10,1,1,1,1])