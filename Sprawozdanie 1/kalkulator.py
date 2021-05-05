print("hello world")
print("==========")
print("Kalkulator")
print("==========")
print("Dodawanie 1")
print("Odejmowanie 2")
print("Mnożenie 3")
print("Dzielenie 4")
print("==========")
x=int(input("Podaj x "))
y=int(input("Podaj y "))
print("==========")
d=int(input("Podaj typ działania (1-4) "))
if d==1:
    wynik=x+y
elif d==2:
    wynik=x-y
elif d==3:
    wynik=x*y
elif d==4:
    if y!=0:
        wynik=x/y
    else:
        print("Błąd, nie dziel przez 0")
        input()
        exit()
print("wynik: "+str(wynik))