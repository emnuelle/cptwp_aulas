# Peça para o usuário digitar a média de "matemática" e exiba se ele foi aprovado (nota maior ou igual a 6) oou reprovado (nota iinferior a 5)
# >= 6 (aprovado)
#  < 6 (reprovado)

print("Vamos descobrir se você foi aprovado em mateática?")
print("Digite a sua média: ")
media = int(input())

if media >= 6 : 
    print("Parabéns, você foi aprovado!")
else : 
    if media < 6 :
        print("Reprovado! Tente fazer melhor da próxima vez :)")

print("FIM!")