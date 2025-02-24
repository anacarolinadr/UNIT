# A LOTOFACIL consiste na extração de 15 números aleatórios diferentes, no universo de 01 a 25. 
# Você marca entre 15 a 18 números, dentre os 25 disponíveis no volante, 
# e fatura o prêmio se acertar 11, 12, 13, 14 ou 15 números. 
# Pode ainda deixar que o sistema escolha os números para você por meio da Surpresinha. 
# Considerando estas informações, faça um programa em Python para:

# a) Solicitar ao usuário a quantidade de dezenas que ele deseja marcar na primeira aposta (entre 15 e 18 números).
# Caso o usuário informe uma quantidade de dezenas fora do intervalo válido, 
# o programa deve solicitar nova digitação, tantas vezes quantas forem necessárias;

# b) Solicitar ao usuário informar os números da primeira aposta (dezenas de 01 a 25, sem repetição). 
# Caso o usuário informe um número repetido, o programa deverá apresentar uma mensagem “Número repetido” 
# e solicitar nova digitação. Assim como se o usuário informar um número fora do intervalo válido,
# o programa deverá apresentar uma mensagem “Dezena inválida” e solicitar nova digitação.

# c) Gerar aleatoriamente duas apostas, com 18 números, usando a “Surpresinha”.

# d) Simular o resultado (15 dezenas sorteadas) de um concurso da Lotofácil;

# e) Imprimir (em ordem crescente) as dezenas da primeira aposta, 
# das duas apostas (surpresinha) e do resultado do concurso da Lotofácil simulado.

import random

# Camada Domínio
class ValoresLotofacil:
    def __init__(self, qtd_dezenas, nums_aposta):
        self.qtd_dezenas = qtd_dezenas
        self.nums_aposta = nums_aposta

# Camada de Serviço
class Lotofacil:
    def __init__(self):
        self.qtd_dezenas = 0
        self.nums_aposta = []
        self.surpresinhas = []
        self.nums_sorteio = []
        self.acertos_aposta = []
        self.acertos_surpresinha1 = []
        self.acertos_surpresinha2 = []

    def definir_aposta(self, valores_lotofacil):
        self.qtd_dezenas = valores_lotofacil.qtd_dezenas
        self.nums_aposta = valores_lotofacil.nums_aposta

    def gerar_surpresinhas(self):
        for _ in range(2):
            surpresinha = sorted(random.sample(range(1, 26), k=18))
            self.surpresinhas.append(surpresinha)
        return self.surpresinhas

    def gerar_sorteio(self):
        self.nums_sorteio = sorted(random.sample(range(1, 26), k=15))
        return self.nums_sorteio

    def checar_acertos(self):
        nums_aposta_set = set(self.nums_aposta)
        nums_sorteio_set = set(self.nums_sorteio)
        surpresinha1_set = set(self.surpresinhas[0])
        surpresinha2_set = set(self.surpresinhas[1])
        
        self.acertos_aposta = nums_aposta_set.intersection(nums_sorteio_set)
        self.acertos_surpresinha1 = surpresinha1_set.intersection(nums_sorteio_set)
        self.acertos_surpresinha2 = surpresinha2_set.intersection(nums_sorteio_set)
        
        return self.acertos_aposta, self.acertos_surpresinha1, self.acertos_surpresinha2

# Camada de Interface: entrada e saída de dados
class InterfaceLotofacil:
    @staticmethod
    def solicitar_dados():  
        while True:
            qtd_dezenas = input("Digite a quantidade de dezenas desejada: (15 a 18) ")

            try:
                qtd_dezenas = int(qtd_dezenas)
                if qtd_dezenas >= 15 and qtd_dezenas <= 18:
                    break
                else:
                    print("Valor inválido para quantidade, digite um valor entre 15 a 18")

            except ValueError:
                print("Valor inválido para quantidade, digite um número")

        nums_aposta = []
        while len(nums_aposta) < qtd_dezenas:
            print(f"Número {len(nums_aposta) + 1}")
            num_aposta = input("Digite um número para sortear: (1 a 25) ")

            try:
                num_aposta = int(num_aposta)

                if num_aposta in nums_aposta:
                    print("Número repetido")
                    continue
                elif 1 <= num_aposta <= 25:
                    nums_aposta.append(num_aposta)
                else:
                    print("Dezena inválida, digite um número entre 1 a 25 inteiro")

            except ValueError:
                print("Valor inválido para número, digite um valor numérico")

        nums_aposta.sort() 
        return ValoresLotofacil(qtd_dezenas, nums_aposta)
    
    @staticmethod
    def imprimir_resultados(self):
        print(f"\nRESULTADO SORTEIO")
        print(f"Seus {self.qtd_dezenas} números escolhidos: \n{self.nums_aposta}")
        print(f"Suas surpresinhas foram:\n1- {self.surpresinhas[0]}\n2- {self.surpresinhas[1]}")
        print(f"Os números sorteados foram:\n{self.nums_sorteio}")
        print(f"Os números certos da sua aposta foram: \n{self.acertos_aposta}")
        print(f"Os números certos da surpresinha 1 foram: \n{self.acertos_surpresinha1}")
        print(f"Os números certos da surpresinha foram: \n{self.acertos_surpresinha2}")

# Camada de Apresentação
def main():
    interface = InterfaceLotofacil()
    lotofacil = Lotofacil()

    print("\nBem-vindo à Loteria!")
    valores = interface.solicitar_dados()
    lotofacil.definir_aposta(valores)
    lotofacil.gerar_surpresinhas()
    lotofacil.gerar_sorteio()
    lotofacil.checar_acertos()
    interface.imprimir_resultados(lotofacil)

if __name__ == "__main__":
    main()