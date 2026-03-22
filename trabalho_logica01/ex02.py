anoatual = int(input('Ano atual: '))
nascimento = int(input('Ano de nascimento : '))
idade = anoatual - nascimento
if idade < 16:
    print('Não tem permissão para o voto.')
elif 18 > idade >= 16 :
    print('Voto opcional.')
else:
    print('Voto obrigatório.')