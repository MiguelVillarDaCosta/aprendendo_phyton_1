#Teste do Uso do Input e If

n = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
#Definição de váriaveis 
soma = n + n2
divs = n / n2
subs = n - n2
mult = n * n2
sobr = n % n2 #sobra ("Divisão")
divint = n // n2 #Divisão inteira
pot = n ** n2 #Potenciação Exemplo: 2*2
raiz = pow(n, 0.5 )# Raiz "Pow" é novo em 
#Calculadora simples com operadores de soma, subtração, divisão e multiplicação, entre outros 
print ('a soma e: ', soma)
print ('a subtracao e: ', subs)
print ('a divisao e: ', divs)
print ('a multiplicacao e: ', mult)
print ('a potenciacao de: ', pot)
print ('a raiz de n1 e: ', raiz)
print ('a divisao inteira de n1 e: ', divint)
print ('a sobra de n1 por n2 e: ', sobr)

print ('===============================================================================')
print ('Seja Bem-Vindo ao sistema de indentificação de Horario simples criado por MIM') #organização vale muito 
print ('===============================================================================')

hr = int(input('digite um horario: ')) # Apenas o Leia do Portugol kksksksksk

if hr < 12: #importante lembrar que o If aqui usa apenas o ":" como divisor da estrutura e do comando em sí
    print ('Good Morning Sir!!')
elif hr <= 16: #Funciona igual ao Else if do C#
    print ('Good Afrternon Sir :)')
else: #Apenas em casos onde nenhuma das condições foi cumprida ou execultado
    print ('Good Night Sir >;)')

#importante ressaltar o uso de parenteses para divisão no calculo da media e afins por exemplo (10+10+10)/3 não 10+10+10/3 já que caso o utimo exemplo seja
#o código acabará por compreender a conta como uma expressão matemática e efetuará na ordem de expressão ou seja, primeiro a divisão


