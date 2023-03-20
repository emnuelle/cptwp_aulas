# Peça para o usuário digitar a média de matemática e exiba se ele foi aprovado (nota maior ou igual a 6), se está em recuperação (nota entre 5,9 e 5) ou reprovado (nota inferior a 5)
# >= 6 (aprovado)
# <+ 5.0 (em recuperação)
# < 5 (reprovado)

print("Vamos descobrir se você foi aprovado!")
print("Digite a sua media: ")
media = float(input())

if media >= 6 :
    print("Parabéns, vocês está aprovado!")
else :
    if media >= 5.0 :
        print("Você está de recuperação, fique de olho nas novas avaliações!")
    elif media < 5 :
        print("Você foi reprovado! Tente de novo")

print("FIM!")