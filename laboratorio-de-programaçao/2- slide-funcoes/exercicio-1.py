# Utilizando as bibliotecas de funções do Python, escreva
# um programa que sorteie os seis números da Mega-Sena e os apresente
# em ordem crescente. Os números não podem ser repetidos

# Como os exercícios eram mais simples, resolvi não utilizar POO pois apenas complicaria o código

import random

def sortear(num_sorteados, inicio, fim):
    sorteio = sorted(random.sample(range(inicio, fim), k=num_sorteados))
    return sorteio

print(sortear(6, 1, 61))
print(sortear(6, 1, 61))
print(sortear(6, 1, 61))
print(sortear(6, 1, 61))

