# dados do jogo, nome e posição dos quartos.

print('HOTEL DOS ANIMAIS')
print('Especificando posição')
print('[1,2,3,4]\n[5,6,7,8]\n')

cont = 1
'''
desenvolvimento do jogo, de acordo com as respostas do usuário o jogador vai 
avançando de fase, caso ele acerte, o sistema irá informar que ele passou para
a proxima fase, se ele errar, o sistema vai informar que ele perdeu e vai se 
encerrar.
'''

# fase 01
while cont <= 4:
    if cont == 1:
        print('\nBem vindo a fase 1! \nNa fase 1, o jogador deve alocar o '
              'RATO e o GATO na seguinte matriz que representam os quartos:')
        print("['*', '*', '-', 'G']\n['R', '-', '*', '*']")

        r = int(input('em qual posição quer alocar o RATO?'))
        g = int(input('em qual posição quer alocar o GATO?'))

        if r == 6 and g == 3:
            print('\nVocê passou para proxima fase!')
            cont += 1
        else:
            print('\nVocê perdeu!!!')
            break
    # fase 02
    elif cont == 2:
        print('\nBem vindo a fase 2!\nNa fase 2, o jogador deve alocar: '
              'CÃO, CÃO E OSSO')
        print("['-','*','*','*']\n['*','C','-','-']")
        c1 = int(input('em qual posição quer alocar o CÃO? '))
        c2 = int(input('em qual posição quer alocar o CÃO? '))
        o = int(input('em qual posição quer alocar o OSSO? '))
        if (c1 == 7 or c1 == 8) and (c2 == 7 or c2 == 8) and o == 1:
            print('\nVocê passou para proxima fase!')
            cont += 1
        else:
            print('\nVocê perdeu!!!')
            break
    # fase 03
    elif cont == 3:
        print('\nBem vindo a fase 3!\nNa fase 3, o jogador deve alocar: '
              'GATO, RATO E OSSO')
        print("['-','*','*','*']\n['-','G','-','*']")
        g = int(input('em qual posição quer alocar o GATO? '))
        r = int(input('em qual posição quer alocar o RATO? '))
        o = int(input('em qual posição quer alocar o OSSO? '))
        if (g == 5 or g == 7) and (o == 5 or o == 7) and r == 1:
            print('\nVocê passou para proxima fase!')
            cont += 1
        else:
            print('\nGame OVocê perdeu!!!')
            break
    # fase 04
    elif cont == 4:
        print('\nBem vindo a fase 4!\nNa fase 4, o jogador deve alocar: '
              'QUEIJO, QUEIJO E OSSO')
        print("['-','-','-','*']\n['*','R','*','*']")
        q1 = int(input('em qual posição quer alocar o QUEIJO? '))
        q2 = int(input('em qual posição quer alocar o QUEIJO? '))
        o = int(input('em qual posição quer alocar o OSSO? '))
        if (q1 == 1 or q1 == 3) and (q2 == 1 or q2 == 3) and o == 2:
            print('\nVoce Venceu!')
            cont += 1
        else:
            print('\nVocê perdeu!!!')
            break
    else:  # mensagem que o usuário recebe caso tenha perdido o jogo!
        print('\nVocê perdeu!!!')
        break