# jogo de adivinhação de números de 1 a 100 com 10 tentativas

from random import *
rdn = randint(0,100)
tent = 10
print()
print("Tente adivinhar um número secreto de 1 a 100! Você terá 10 tentativas.")
print()
while tent > 0:
    tent = tent - 1
    ch = int(input("Qual o seu palpite? "))
    if ch > rdn:
        print("O número secreto é menor!")
        print("Numero de tentativas: %d" % tent)
        print()
    elif ch < rdn:
        print("O número secreto é maior!")
        print("Numero de tentativas: %d" % tent)
        print()
    else:
        print("Parabéns! Você acertou, o número secreto é: %d" % rdn)
        tent = -1
    if tent == 0:
        print()
        print("Que pena! Você perdeu! Mais sorte da próxima vez!")
        print("O número secreto é: %d" % rdn)
        input()
    elif tent == -1:
        input()
