a = float(input("Ingrese el coeficiente cuadratico:\n"))
b = float(input("Ingrese el coeficiente lineal:\n"))
c = float(input("Ingrese el termino independiente:\n"))
disc = b*b - 4*a*c
if disc > 0:
    print("la ecuacion tiene dos soluciones diferentes (x1 != x2)")
elif disc == 0:
    print("la ecuacion tiene una unica solucion (x1 = x2)")
else :
    print("la ecuacion tiene solucion(es) en los Imaginarios")