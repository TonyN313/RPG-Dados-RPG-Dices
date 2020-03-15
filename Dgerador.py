import random

while True:
    print("Bem vindo !")
    print("Esse é o gerador de dados.")
    print("Quais dados você quer usar?")
    print("'d4','d6' ou 'd20'?")
    print("Se não quiser usar, digite 'sair'.")
    input_usuario = input(": ")

    if input_usuario == "sair":
        break
    elif input_usuario == "d4":
        dados = int(input("Quantos dados irá usar?: "))
        for valor in range (dados)
            valor = random.ramdint(1,4)
            print(valor)        
