# Definindo Variaveis abaixo lembrando que o python é uma linguagem dinâmica 
nome = "Miguel Villar"
idade = 16
altura = 1.80
situacao = False #comentários podem ser acessados pelo atalho cltr+;

print('hello word')
print('A soma seria:',2+3) 
print('A subtracao e:',5-6)
print('A multiplicacao e: {}'.format(5*5))
print(f'A Divisao é: {10/2}')
# Mais ultilizados , f e .format(conta), com o f sendo o mais ultilizado e mais conveniente 
print (f'seu nome e: {nome} sua idade e: {idade} sua altura e: {altura} sua situacao de trabalho e: {situacao}')

name = input("coloque seu nome:")
print(f"seu nome é {name}")
# O código acima consegue ler váriaveis (OBS: para melhor entendimento é melhor checar o funcionamento do input)