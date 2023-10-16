'''nome = input('digite o seu nome: ')
if nome == 'paza':
    print('que nome bonito você tem!')
else:
    print('que nome comum e chato......')

print('seja bem-vindo(a) {}!'.format(nome)) '''


'''nota1 = float(input('digite a primeira nota do aluno: '))
nota2 = float(input('digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if media >= 7.0:
    print('\nAprovado!! <3')
else:
    print('\nReprovado!! :(')

print('A media do aluno foi {}'.format(media))'''


nota1 = float(input('digite a primeira nota do aluno: '))
nota2 = float(input('digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

print('\nAprovado!' if media >= 7.0 else '\nReprovado!')
print('A media do aluno foi {}'.format(media))





