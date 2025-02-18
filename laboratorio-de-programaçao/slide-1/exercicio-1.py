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

class CadastroCliente:

    def __init__(self):
        self.nome = ""
        self.sexo = ""
        self.placa = ""
        self.km_contratados = 0
        self.dias_contratados = 0
        self.valor = 0
        self.lista_clientes = []

    def conferir_nome(self):
        while True:
            nome = input("Nome completo: ").strip()
            if nome:
                self.nome = nome
                return self.nome
            print("Nome inválido, digite novamente")

    def conferir_sexo(self):
        while True:
            sexo = input("Gênero: (F ou M) ").strip().upper()
            if sexo in ["F", "M"]:
                self.sexo = sexo
                return self.sexo
            else: 
                print("Gênero inválido, digite novamente (F ou M)")

    def conferir_placa(self):
        while True:
            placa = input("Placa do veículo: ").strip().upper()
            if len(placa) == 7 and placa[:3].isalpha():
                formato_antigo = placa[3:].isdigit() #LLLNNNN - formato antigo das placas
                formato_novo = placa[3].isdigit() and placa[4].isalpha() and placa[5:].isdigit() #LLLNLNN - formato novo das placas
                
                if formato_antigo or formato_novo:
                    self.placa = placa
                    return self.placa
            
            print("Formato inválido. Use o padrão ABC1234 ou ABC1D23")

    def conferir_km(self):
        while True:
            km_contratados = input("Quantidade de quilômetros contratados: ").strip().lower()
            if km_contratados.endswith("km"):
                km_contratados = km_contratados[:-2] 
            
            try:
                km_contratados = float(km_contratados)
                if km_contratados >= 1:
                    self.km_contratados = km_contratados
                    return self.km_contratados
                else:
                    print("Valor inválido para quilometragem, digite um valor inteiro")

            except ValueError:
                print("Valor inválido para quilometragem, digite um número")

    def conferir_dias(self):
        while True:
            dias_contratados = input("Quantidade de dias contratados: ").strip()
            try:
                dias_contratados = float(dias_contratados)
                if dias_contratados >= 1:
                    self.dias_contratados = dias_contratados
                    return self.dias_contratados
                else:
                    print("Valor inválido para dias, digite um valor inteiro")

            except ValueError:
                print("Valor inválido para dias, digite um número")
    
    def calcular_valor(self):
        valor = (self.dias_contratados * 70) + (self.km_contratados * 0.1)
        self.valor = valor
        return self.valor
    
    def adicionar_cliente(self):

        nome = self.conferir_nome()
        sexo = self.conferir_sexo()
        placa = self.conferir_placa()
        km_contratados = self.conferir_km()
        dias_contratados = self.conferir_dias()
        valor = self.calcular_valor() 

        cliente = {
            "nome": nome,
            "sexo": sexo,
            "placa": placa,
            "km_contratados": km_contratados,
            "dias_contratados": dias_contratados,
            "valor": valor
        }

        self.lista_clientes.append(cliente)
        print("\nCliente cadastrado com sucesso!")
        return self.lista_clientes
     
    def imprimir_valor(self):
        if not self.lista_clientes:
            print("Não há clientes cadastrados no sistema.")
            return
        print("\nLista de Clientes:")
        for i, cliente in enumerate(self.lista_clientes, 1):
            print(f"Cliente {i}")
            print(f"Placa do carro: {cliente['placa']}")
            print(f"Valor total: R$ {cliente['valor']:.2f}")
        
    def imprimir_media_km(self):
        if not self.lista_clientes:
            print("Não há clientes cadastrados no sistema.")
            return
        
        soma_km = sum(cliente['km_contratados'] for cliente in self.lista_clientes)
        media = soma_km / len(self.lista_clientes)
    
        print("\nEstatísticas de Quilometragem:")
        print(f"Média dos quilômetros contratados: {media:.2f} km ")

    def imprimir_mulheres_aluguel_7_dias(self):
        if not self.lista_clientes:
            print("Não há clientes cadastrados no sistema.")
            return

        encontrou_mulheres = False
        for cliente in self.lista_clientes:
            if cliente["sexo"] == "F" and cliente["dias_contratados"] > 7:
                print(f"Cliente: {cliente['nome']}")
                encontrou_mulheres = True
        
        if not encontrou_mulheres:
            print("Não há mulheres com aluguéis acima de 7 dias.")

def main():
    cadastro = CadastroCliente()

    while True:
        print("\nBem-vindo à Locadora de Veículos!")
        print("Digite o número da opção desejada:")
        print("1- Adicionar um novo cliente ao sistema")
        print("2- Listar as placas cadastradas e os respectivos valores")
        print("3- Calcular média dos quilômetros rodados por clientes")
        print("4- Listar clientes mulheres que alugaram acima de 7 dias")
        print("5- Sair \n")
        
        opcao_usuario = input("Número da opção: ")

        if opcao_usuario == "1" or opcao_usuario.lower() == "um":
            cadastro.adicionar_cliente()
        elif opcao_usuario == "2" or opcao_usuario.lower() == "dois":
            cadastro.imprimir_valor()
        elif opcao_usuario == "3" or opcao_usuario.lower() == "tres":
            cadastro.imprimir_media_km()
        elif opcao_usuario == "4" or opcao_usuario.lower() == "quatro":
            cadastro.imprimir_mulheres_aluguel_7_dias()
        elif opcao_usuario == "5" or opcao_usuario.lower() == "sair":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, digite novamente")

if __name__ == "__main__":
    main()