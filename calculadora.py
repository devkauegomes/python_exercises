# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")
print('\nSelecione o número da operação desejada:')
print('\n1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

#Definindo funções para as operações.
soma = lambda x,y: print(f'{x} + {y} = {x+y}')
subtracao = lambda x,y: print(f'{x} - {y} = {x-y}')
multiplicacao = lambda x,y: print(f'{x} * {y} = {x*y}')
divisao = lambda x,y: print(f'{x} / {y} = {x/y}')

#Definindo função para perguntar os dois valores ao usuário e retorná-los.
def pergunta_numeros():
    x = float(input('\nDigite o primeiro número: '))
    y = float(input('\nDigite o segundo número: '))
    return x,y

#Início do programa e verificação de erro no momento do input do operador.
try:
    operacao = int(input('\nDigite sua opção (1/2/3/4): '))
    if operacao == 1:
        x,y = pergunta_numeros()
        soma(x,y)
    elif operacao == 2:
        x,y = pergunta_numeros()
        subtracao(x,y)
    elif operacao == 3:
        x,y = pergunta_numeros()
        multiplicacao(x,y)
    elif operacao == 4:
        x,y = pergunta_numeros()
        divisao(x,y)
    else:
        print('O valor digitado é inválido, encerrando programa...')
        
except ValueError:
    print('O valor digitado é inválido, encerrando programa...')