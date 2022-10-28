cadastro = {'nome':[], 'sexo':[], 'ano':[]}
    nome = input('Qual seu nome ?')
    sexo = input('Qual seu sexo [M/F]?')
    ano  = int(input('qual seu ano de nascimento?'))
cadastro['nome'].append(nome)
cadastro['sexo'].append(sexo.upper())
cadastro['ano'].append(ano)

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]: ')
    if terminar.upper() in 'N' :
        break
    if terminar.upper() not in 's' :
        print('Digite S para SIM ou N para NÂO')
        continue

print(cadastro)

