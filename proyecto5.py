a =int(input("Ingrese las Horas:\n"))
b =int(input("Ingrese los Minutos:\n"))
c =int(input("Ingrese los Segundos:\n"))
d = c + 1
if d > 59:
    e = b + 1 
    d = 00
    if e > 59:
        f = a + 1
        e = 00
        if f > 23:
            g = 00
            print("La hora es:\n",g,":",e,":",d)
        else:
             print("La hora es:\n",f,":",e,":",d)
    else:
        print("La hora es:\n",a,":",e,":",d)
else: 
    print("la hora es:\n",a,":",b,":",d)