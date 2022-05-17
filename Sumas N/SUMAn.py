"""Suma de N naturales"""

print("--------------------------------------------")
print("-----------Calcula el valor de N------------")
print("--------------------------------------------")

#Input
N = int(input("Digite el valor de N: "))

#Processing
i = 1
suma = 0
while (i <= N):
    suma = suma + i
    i = i + 1

#Output
print("La suma de los " + str(N) + " primeros naturales es: " + str(suma))

#Fin