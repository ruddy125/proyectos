a =int(input("Ingrese el tiempo X en segundos:\n"))
b =int(input("Ingrese las horas de Z:\n")) 
c =int(input("Ingrese los minutos de Z:\n"))
d =int(input("Ingrese los segundos de Z:\n"))
e = b*3600 + c*60 + d
if e > a:
    print("No se puede completar la tarea en el tiempo X")
else: 
    print("Se puede completar la tarea en el tiempo X")