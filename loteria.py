import random

numeros = [x for x in range(1,16)]
numero_sorteado = random.choice(numeros)

total_tentativas = 3

while total_tentativas > 0:

    while True:

        try:
            tentativa = int(input('\nDigite um número: '))
        except ValueError as err:
            print('Valor inválido!')
            continue
        
        if 1 <= tentativa <= 15:
            break

    if tentativa == numero_sorteado:
        print('\nParabéns, você ganhou a loteria da babilônia!!!')
        break
    elif tentativa < numero_sorteado:
        print('\nO seu chute é menor que o número sorteado.')
        total_tentativas -= 1
        continue
    else:
        print('\nO seu chute é maior que o número sorteado.')
        total_tentativas -= 1

if total_tentativas == 0:
    print('\nVocê Perdeu!')

print('\nObrigado por jogar!')