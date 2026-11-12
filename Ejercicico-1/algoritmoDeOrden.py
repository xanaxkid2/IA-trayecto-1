
## Organizar 3 numeros de menor a mayor

## SOLUCION 1 CON INPUT


num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")
num3 = input("Ingrese el tercer número: ")

if num1 <= num2 and num1 <= num3:
    menor = num1
    if num2 <= num3:
        medio = num2
        mayor = num3
    else:
        medio = num3
        mayor = num2

elif num2 <= num1 and num2 <= num3:
    menor = num2
    if num1 <= num3:
        medio = num1
        mayor = num3
    else:
        medio = num3
        mayor = num1

else:
    menor = num3
    if num1 <= num2:
        medio = num1
        mayor = num2
    else:
        medio = num2
        mayor = num1


print("Números ordenados de menor a mayor:")
print(menor, medio, mayor)


## SOLUCION 2 - DATOS PREESTABLECIDOS

numeros = [5, 2, 7]

numeros.sort()

print(numeros)