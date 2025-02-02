"""
    Básico: imprime todos los números enteros del 0 al 100.
    Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
    Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
    Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).
    Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
    Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).

"""

for i in range (0, 101):
    print(i)

for i in range (2, 202):
    if i % 2 == 0:
      print(i)

for i in range (0, 101):
    print (i)
    if i % 5 == 0:
        print("ice ice")
        if i % 10 == 0:
            print("baby")

numero = 0
suma = 0
for numero in range(0, 500001, 2):
    suma += numero
    print("La suma de pares del 0 al 500,000 es:", suma)


for i in range (2024, 0, -3):
    print(i)

numInicial = 1
numFinal = 80
multiplo = 5
for i in range (numInicial, numFinal):
        if i % multiplo==0:
            print(i)