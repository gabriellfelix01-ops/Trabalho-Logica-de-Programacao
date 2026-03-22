codigo = int(input('Código do usuário: '))

if codigo != 1234:
    print('Usuário inválido')
else:
    senha = int(input('Senha: '))

    if senha != 9999:
        print('Senha incorreta')
    else:
        print('Acesso permitido')
