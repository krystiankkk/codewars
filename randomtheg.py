import random

pc = random.randint(1, 200)
proba=0

while proba<5:
    wybor = input('Wybierz jakas libczbe\n') # definicja wyboru uzytkownika
    if int(wybor) == pc:    #tu if do porownania wartosci
        print(f'Zgadles za {proba+1} razem z 5 mozliwych')  # komunikat po zgadnięćiu

        quit() # quit-program się kończy
    else:
        print(f'Probuj dalej, to byla twoja {proba+1} próba') # tu else jak trafi za i- razem
        if int(wybor)<pc:
            print('za malo')
        else:
            print('za duzo')
    if proba==4:
        print(f'Nie zgadles, ta liczba to: {pc}')
    proba+=1
