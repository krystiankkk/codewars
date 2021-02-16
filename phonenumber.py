def create_phone_number(n):
    prefix=''
    mid=''
    intern=''
    for i in range(0, 3):
        prefix+=str(n[i])

    for i in range(3,6):
        mid+=str(n[i])

    for i in range(6, 10):
        intern+=str(n[i])
    return f"({prefix}) {mid}-{intern}"