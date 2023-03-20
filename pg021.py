# Peça para o usuário digitar um número interiro qualquer e exiba se o numero digitado é par ou impar

num = resto = 0

print("Vamos descobrir se o seus número é par ou ímpar!")
print("Digite um número")
num = int(input())
resto = num % 2
if resto == 0 :
    print("Seu número é par!")
else:
    print("Seu número é ímpar!")


print("FIM!")

