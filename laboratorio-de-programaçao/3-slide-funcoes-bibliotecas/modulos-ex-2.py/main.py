import functions

while True:
    
    print("Bem vindo! Qual função você deseja: ")
    print("1- Verificar se um número é ímpar ou par")
    print("2- Calcular a média de dois números")
    print("3- Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        num = input("Digite um número: ")
        try:
            num = float(num)
            print(functions.impar_par(num))

        except ValueError:
            print("Valor inválido para opção, digite um número")
    
    elif opcao == "2":
        num1 = input("Digite um número: ")
        num2 = input("Digite outro número: ")
        
        try:
            num1 = float(num1)
            num2 = float(num2)
            print(functions.media(num1, num2))

        except ValueError:
            print("Valor inválido para opção, digite dois números")

    elif opcao.lower() == "3" or "sair":
        break
    
    else:
        print("Número inválido opção, digite 1, 2 ou 3")
