# Você está iniciando um novo negócio: uma locadora de veículos. Para iniciar o
# controle do aluguel de carros é necessário um sistema simples. Dessa forma,
# desenvolva um programa um Python para:

# a) Solicitar ao usuário informações sobre as locações: nome do cliente, sexo (F- Feminino, M -
# Masculino), placa do carro alugado, quantidade de quilômetros contratados, quantidade de dias
# contratados;

# b) Calcular e imprimir a placa do carro e valor total a pagar para CADA cliente, considerando que
# deverá ser cobrado o valor de R$ 70,00 por dia contratado, e R$ 0,10 para cada quilômetro
# contratado;

# c) Calcular e imprimir a média de quilômetros contratados pelos clientes;

# d) Calcular e imprimir o nome das clientes de sexo feminino que fecharam aluguéis acima de 7 dias
# contratados.

# Obs.: o programa encerra quando o usuário informa o texto SAIR.

# Ainda que os exercícios sejam simples, resolvi desenvolê-los com POO a fim de aprimorar meus conhecimentos

# Camada Domínio
class Cliente:
    def __init__(self, nome, sexo, placa, km_contratados, dias_contratados):
        self.nome = nome
        self.sexo = sexo
        self.placa = placa
        self.km_contratados = km_contratados
        self.dias_contratados = dias_contratados
        self.valor = self.calcular_valor()

    def calcular_valor(self):
        return (self.dias_contratados * 70) + (self.km_contratados * 0.1)

# Camada de Serviço
class CadastroCliente:
    def __init__(self):
        self.lista_clientes = []
        self.lista_mulher_aluguel_sete_dias = []
    
    def adicionar_cliente(self, cliente):
        self.lista_clientes.append(cliente)

    def calcular_media_km(self):
        if not self.lista_clientes:
            print("Não há clientes cadastrados no sistema.")
            return 0

        media_km = sum(cliente.km_contratados for cliente in self.lista_clientes) / len(self.lista_clientes)
        return media_km  

    def calcular_mulheres_aluguel_mais_sete_dias(self):
        if not self.lista_clientes:
            print("Não há clientes cadastrados no sistema.")
            return []

        self.lista_mulher_aluguel_sete_dias = [
            cliente for cliente in self.lista_clientes if cliente.sexo == "F" and cliente.dias_contratados > 7
        ]

        return self.lista_mulher_aluguel_sete_dias

# Camada de Entrada de Dados
def solicitar_dados():
    nome = input("Nome completo: ").strip()

    while True:
        sexo = input("Gênero: (F ou M) ").strip().upper()
        if sexo in ["F", "M"]:
            break
        print("Gênero inválido, digite novamente (F ou M)")

    while True:
        placa = input("Placa do veículo: ").strip().upper()
        if len(placa) == 7 and placa[:3].isalpha():
            formato_antigo = placa[3:].isdigit()
            formato_novo = placa[3].isdigit() and placa[4].isalpha() and placa[5:].isdigit()
            if formato_antigo or formato_novo:
                break
        print("Formato inválido. Use o padrão ABC1234 ou ABC1D23")

    while True:
        try:
            km_contratados = float(input("Quantidade de quilômetros contratados: ").strip())
            if km_contratados >= 1:
                break
            print("Valor inválido para quilometragem, digite um número maior que 0")
        except ValueError:
            print("Valor inválido, digite um número")

    while True:
        try:
            dias_contratados = int(input("Quantidade de dias contratados: ").strip())
            if dias_contratados >= 1:
                break
            print("Valor inválido para dias, digite um número maior que 0")
        except ValueError:
            print("Valor inválido, digite um número inteiro")

    return Cliente(nome, sexo, placa, km_contratados, dias_contratados)

# Camada de Apresentação
def main():
    cadastro = CadastroCliente()

    while True:
        print("\nBem-vindo à Locadora de Veículos!")
        print("1- Adicionar um novo cliente ao sistema")
        print("2- Listar as placas cadastradas e os respectivos valores")
        print("3- Calcular média dos quilômetros rodados por clientes")
        print("4- Listar clientes mulheres que alugaram acima de 7 dias")
        print("5- Sair\n")

        opcao_usuario = input("Número da opção: ")

        if opcao_usuario == "1":
            cliente = solicitar_dados()
            cadastro.adicionar_cliente(cliente)
            print("\nCliente cadastrado com sucesso!")

        elif opcao_usuario == "2":
            if not cadastro.lista_clientes:
                print("Não há clientes cadastrados no sistema.")
                continue
            print("\nLista de Clientes:")
            for cliente in cadastro.lista_clientes:
                print(f"Placa: {cliente.placa}\nValor total: R$ {cliente.valor:.2f}")

        elif opcao_usuario == "3":
            media_km = cadastro.calcular_media_km()
            print(f"Média dos quilômetros contratados: {media_km:.2f} km")

        elif opcao_usuario == "4":
            mulheres = cadastro.calcular_mulheres_aluguel_mais_sete_dias()
            if mulheres:
                print("\nLista de clientes mulheres com aluguel acima de 7 dias:")
                for cliente in mulheres:
                    print(f"Nome: {cliente.nome}")
            else:
                print("Não há mulheres com aluguéis acima de 7 dias.")

        elif opcao_usuario == "5":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida, digite novamente.")

if __name__ == "__main__":
    main()