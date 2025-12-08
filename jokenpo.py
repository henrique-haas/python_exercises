from random import randint
print('Vamos jogar JOKENPO!')
num1 = randint(1, 3)
num2 = int(input('Considere:\n[1] Pedra\n[2] Papel\n[3] Tesoura\nDigite sua escolha: '))
if num1 == num2:
    print(f'EMPATE! Você escolheu {num2} e o computador {num1}. Tente novamente!')
elif (num1 == 1 and num2 == 2) or (num1 == 2 and num2 == 3) or (num1 == 3 and num2 == 1):
    print(f'VOCÊ VENCEU! Você escolheu {num2} e o computador {num1}. Parabéns!')
else:
    print(f'VOCÊ PERDEU! Você escolheu {num2} e o computador {num1}. Tente novamente!')