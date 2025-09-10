#para que o cliente possa definir quantidades:#

# numerocli =  int(input("quantidade de clientes que você quer cadastrar"))
# clientes = []
# vetor = [0 for i in range (numerocli)]
# print (numerocli)#Testes do fessor parte 1
# for i in range(numerocli):
#     clientes.insert(i, input("Digite o nome do cliente: "))
# print (clientes)

# #coleta e exibe nomes pré digitados usando dados guardados pelo array 
#"insert" faz com que um valor não pré digitado possa ter um dado armazenado posteriormente quase como input porém usando array 
#Array com estrutura para comportar diversos valores (esquecú o nome desse tipo) == array multidimensional 
#Exemplo
#Nomes 
#Idades
#Cores

# Cliente = [["Jose Carlos", "Bruno", "Camila"],[35,40,15],["Azul","Vermelho","Amarelo"]]
# print(Cliente[0][0])
# print(Cliente[1][0])
# print(Cliente[2][0])

#Parte 3 dos testes e exemplos do fessor (lembrar de revisar isso porém focar no Array simples, visitar a aba docs do python e abrir o tutorial)

# numeroCli = int(input("Digite Quantos clientes você deseja cadastrar"))
# vetor = [0 for i in range (numeroCli)]

# for i in range (numeroCli):
#     print(f"\n Digite os dados da pessoa")
#     nome = input("Nome")
#     idade = input("Idade")
#     sexo = input("Sexo")
#  vetor[i] = {
#      "nome": nome;
#      "idade": idade;
#      "sexo": sexo;
#  }
# print ("\n Lista de pessoas cadastradas")
# for pessoas in vetor:
#     print(pessoas)
#     print()
#     print(vetor[0]["nome"])
from random import randint

print ("digite tres numeros tentando adivinhar os numeros que o computador sortear (1 a 100)")
a = int(input("digite o numero um:> "))
b = int(input("digite o numero dois:> "))
c = int(input("digite o numero tres:> "))
random = randint(1,100)
rando = randint(1,100)
rand = randint(1,100)
if ((a == random)(b == rando)(c == rand)):
    print ("voce ganhou")
else:
    print("voce perdeu")

    