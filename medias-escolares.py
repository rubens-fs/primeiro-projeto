nome = input('Qual é o seu nome? ')
print('É um prazer em te conhecer, {}!'.format(nome))
print('Quais foram as suas 4 notas, respectivamente?')
n1 = float(input('Qual foi a sua Nota 1? '))
n2 = float(input('Qual foi a sua Nota 2? '))
n3 = float(input('Qual foi a sua Nota 3? '))
n4 = float(input('Qual foi a sua Nota 4? '))
s = (n1 + n2 + n3 + n4)/4  # Cálculo para a média: Somando todas as 4 (quatro) notas e dividindo por 4 (quatro).
print('A média das notas {0}, {1}, {2} e {3} é {4}!'.format(n1, n2, n3, n4, s))
if s >= 7:  # Se a nota for maior ou igual a 7 (sete), irá mostrar que o(a) aluno(a) foi aprovado(a).
    print('Parabéns, você foi aprovado(a)!')
    print('Boas férias!')
else:  # Se a nota for menor que 7 (sete), irá mostrar uma mensagem que o(a) aluno(a) foi reprovado(a).
    print('Infelizmente você foi reprovado(a)!')
    print('Lembrando que as datas da recuperação serão marcadas na coordenação do seu bloco. Bons estudos!')
