valor = int(input('Digite o valor em R$'))

if valor >= 100:
    cedulas100 = valor // 100
    valor -= cedulas100 * 100
    print('cedulas de 100: {}'.format(cedulas100))
if valor >= 50:
    cedulas50 = valor // 50
    valor -= cedulas50 * 50
    print('cedulas de 50: {}'.format(cedulas50))
if valor >= 20:
    cedulas20 = valor // 20
    valor -= cedulas20 * 20
    print('cedulas de 20: {}'.format(cedulas20))
if valor >= 10:
    cedulas10 = valor // 10
    valor -= cedulas10 * 10
    print('cedulas de 100: {}'.format(cedulas10))
if valor >= 5:
    cedulas5 = valor // 5
    valor -= cedulas5 * 5
    print('cedulas de 5: {}'.format(cedulas5))
if valor:
    cedulas1 = valor
    print('cedulas de 1: {}'.format(cedulas1))