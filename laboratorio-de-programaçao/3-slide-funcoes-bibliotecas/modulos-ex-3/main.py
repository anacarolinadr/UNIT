# O programa principal deve enviar parâmetros para as funções conforme a entrada
# do usuário e retornar o valor calculado da área de acordo com a escolha do tipo de
# objeto do usuário.
# O programa principal também deve ter um menu de opções que irá levar ao
# cálculo da área de cada tipo de objeto.

# 1 - Retângulo
# 2 - Triângulo
# 3 - Círculo
# 0 - Sair

import functions

while True:

    print("Bem vindo! Qual forma geométrica você deseja encontrar a área: ")
    print("1- Retângulo")
    print("2- Triângulo")
    print("3- Círculo")
    print("0- Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        base = input("Digite a base do retângulo: ")
        altura = input("Digite a altura do retângulo: ")
        try:
            base = float(base)
            altura = float(altura)
            print(f"{functions.area_retangulo(base, altura)}\n")

        except ValueError:
            print("Valor inválido para base ou altura, digite um número")
    
    elif opcao == "2":
        base = input("Digite a base do triângulo: ")
        altura = input("Digite a altura do triângulo: ")
        try:
            base = float(base)
            altura = float(altura)
            print(f"{functions.area_triangulo(base, altura)}\n")

        except ValueError:
            print("Valor inválido para base ou altura, digite um número")
    
    elif opcao == "3":
        raio = input("Digite o raio do círculo: ")
        try:
            raio = float(raio)
            print(f"{functions.area_circulo(raio)}\n")

        except ValueError:
            print("Valor inválido para raio, digite um número")
    
    elif opcao.lower() == "0" or opcao.lower() == "sair":
        break
    
    else:
        print("Número inválido opção, digite 1, 2, 3 ou 0 (sair) \n")