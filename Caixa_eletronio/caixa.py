total = 500
opcao = int(input('Qual opcão você deseja:'))
if opcao == 1:
    saque = int(input('Quanto deseja saquar:'))
    if saque <= total:
        total -= saque
        print(f'Você sacou R${saque} e ainda tem em conta R${total}')
    if saque > total:
        print('SALDO INSUFICIENTE!')
if opcao == 2:
    nomefav = str(input('Dígite o nome do favorecido:')).strip()
    print('Quanto deseja transferir?')
    valorfav = int(input('Dígite o valor:'))
    if valorfav <= total:
        total -= valorfav
        print(f'Você transferiu R${valorfav} para o Sr(a). {nomefav} ainda tem R${total} em conta')
if opcao == 3:
    print('Quanto deseja depositar?')
    deposito = int(input('Dígite valor do deposito:'))
    total += deposito
    print(f'Você depositou R${deposito} e o total em conta é de R${total}')