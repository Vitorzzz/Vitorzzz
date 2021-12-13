print('calculadora')
print('+ Adição')
print('- Subtração')
print('* multiplicação')
print('/ divisão')
print('Pressione outra tecla para sair')
op = input('qual operação deseja fazer?')
if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input('Digite o primeiro valor:'))
    y = int(input('Digite o segundo valor:'))
while (op != 'sair'):
    if (op == '+'):
        res = x + y
        print('Resultado: {} + {} = {}'.format(x, y, res))
    elif (op == '-'):
        res = x - y
        print('Resultado: {} - {} = {}'.format(x, y, res))
    elif(op == '*'):
        res = x * y
        print('Resultado: {} * {} = {}'.format(x, y, res))
    elif(op == '/'):
        res = x / y
        print('Resultado: {} / {} = {}'.format(x, y, res))
    else:
        print('Operação invalida')

    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite o primeiro valor:'))
        y = int(input('Digite o segundo valor:'))
print('Encerrando o programa....')