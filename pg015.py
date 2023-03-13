# Realizando uma equação do segundo grau

# a=3, b=7, c=2, x1=2, x2=0.3

import math

print("informe o valor de a: ")
a = int(input())

print("Informe o valor de b: ")
b = int(input())

print("informe o valor de c: ")
c = int(input())

(delta) = (b * b) - (4 * a * c)

print("O valor de delta é: ", delta)

x2 = (-b + math.sqrt(delta)) / (2 * a)
y1 = (-b - math.sqrt(delta)) / (2 * a)

print("Seu valor de X é: ", x2)
print("Seu valor de Y é: ", y1)



