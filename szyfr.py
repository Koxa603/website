from random import*
from time import*
print("URUCHOMIANIE")
sleep(1)
print("Przygotowywanie szyfru\n")
print("0   %")
for i in range(1,4):
    print(i*20," %")
    sleep(0.3)
print("80  %")
sleep(1.5)
print("100 %\nGOTOWE\n")
while(True):
    sleep(2)
    print("")
    print("Co chcesz zrobić odszyfrować czy za szyfrować wiadmość")
    print("(Napisz 'zasz' aby zaszyfrować lub 'odsz' aby odszyfrować)")
    w=input("lub 'x' aby zakończyć działanie programu)\n ")
    if(w=="zasz"):
        r=randrange(2,100)
        r-=r%3
        r=str(r)
        print("")
        slowo=input(" Podaj zdanie do zaszyfrowania (W jednej lini): ")
        i=0
        sl=""
        while(i<len(r)):
            sl+=str(chr(((ord(r[i])+(7+2*(i%3)-32))%94)+32))
            i+=1
        print('')
        print(" Zaszyfrowana wiadomość: ")
        print(sl)
        i=0
        sl=""
        r=int(r) 
        while(i<len(slowo)):
            sl+=str(chr(((ord(slowo[i])+(7+2*(i%r)-32))%94)+32))
            i+=1
        print(sl)
        print("")
    elif(w=="odsz"):
        print("")
        r=input(" Podaj zdanie do odszyfrowania(Dwie linie): ")
        slowo=input()
        i=0
        sl=""
        while(i<len(r)):
            sl+=str(chr(((ord(r[i])-32)+32-(7+2*(i%3))-32)%94+32))
            i+=1
        i=0
        try:
            r=int(sl)
        except ValueError:
            print("")
            print("Odszyfrowana wiadomość: ")
            print("abcdefghijklmnpqrstuvwxyz")
            continue
        sl=""
        while(i<len(slowo)):
            sl+=str(chr(((ord(slowo[i])-32)+32-(7+2*(i%r))-32)%94+32))
            i+=1
        print("")
        print("Odszyfrowana wiadomość: ")
        print(sl)
    elif(w=='x'):
        print("")
        print("WYŁĄCZNIE")
        for i in range(1,5):
            print(i*25,"%")
            sleep(0.4)
        print("Do widzenia!")
        sleep(2)
        break
        
