def equalsides(list):
    for i in range(len(list)):
        if sum(list[:i]) == sum(list[i+1:]):
            return i
        else:
            return -1

