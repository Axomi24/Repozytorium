print("==========")
print("Kalkulator")
print("==========")
print("Dodawanie 1")
print("Odejmowanie 2")
print("Mnożenie 3")
print("Dzielenie 4")
print("Potęgowanie 5")
print("==========")
x=int(input("Podaj x "))
y=int(input("Podaj y "))
print("==========")
d=input("Podaj typ działania (1-5) ")
if d=='1':
    wynik=x+y
elif d=='2':
    wynik=x-y
elif d=='3':
    wynik=x*y
elif d=='4':
    if y!=0:
        wynik=x/y
    else:
        print("Błąd, nie dziel przez 0")
        input()
        exit()
elif d=='5':
    wynik=pow(x,y)
else:
    print("Błąd, zły typ działania")
    input()
    exit()

print("wynik: "+str(wynik))