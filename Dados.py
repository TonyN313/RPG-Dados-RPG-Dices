from random import randint

while True:
    print('-=-' * 10)
    print('Gerador de Dados')
    print('-=-' * 10)
    print('Bem vindo\n')
    print('Qual dado você quer usar?')
    print(" 'D4'\n 'D6'\n 'D8'\n 'D10'\n 'D12'\n 'D20'\n 'D%'\n")
    print('Senão, digite "sair"')
    input_usuario = input("")

    if input_usuario == "sair":
        break

    elif input_usuario == 'D4':
        Valor = random.randint(1,4)
        print('O valor do dado foi {}\n'.format(Valor))

    elif input_usuario == 'D6':
        Valor = random.randint(1,6)
        print('O valor do dado foi {}\n'.format(Valor))

    elif input_usuario == 'D8':
        Valor = random.randint(1,8)
        print('O valor do dado foi {}\n'.format(Valor))

    elif input_usuario == 'D10':
        Valor = random.randint(1,10)
        print('O valor do dado foi {}\n'.format(Valor))

    elif input_usuario == 'D12':
        Valor = random.randint(1,12)
        print('O valor do dado foi {}\n'.format(Valor))

    elif input_usuario == 'D20':
        Valor = random.randint(1,20)
        print('O valor do dado foi {}\n'.format(Valor))

    elif input_usuario == 'D%':
        Valor = random.randint(1,100)
        print('O valor do dado foi {}\n'.format(Valor))
