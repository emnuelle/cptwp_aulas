# Faça um programa para um usuário digitar a sua idade e exiba se ele é obrigado a votar ou nâo
# idade > 18 (obrigadoo a votar)
# idade < 18 (não é obrigado a votar)

idade = 0
print("Descubra se você é obrigado a votar ou não!")
print("Digite a sua idade: ")
idade = int(input())

if idade >= 18 :
    print("Você é obrigado a votar, regularize o seu título para não precisar pagar multas")
else :
    print("Não precisa votar :) APPOVEITE!")

print("Fim! :p")