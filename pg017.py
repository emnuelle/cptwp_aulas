# Peça para o usuário digittar a sua idade e exiba se ele é obrigado a votar, se ele pode votar e se ele não pode votar
# > 18 (obrigado a votar)
# >= 16 e < 18 (pode mas se quiser)
# < 16 (não pode)

idade = 0 

print("Descubra se você ja é apto para votar!")
print("Digite a sua idade: ")
idade = int(input())
if idade >= 18 :
    print("Obrigatório votar! ESCOLHA BEM O SEU CANDIDATO")
else : 
    if idade < 16 :
        print("Não pode votar! APROVEITE")
    else :
        print("Pode votar, se quiser!")
