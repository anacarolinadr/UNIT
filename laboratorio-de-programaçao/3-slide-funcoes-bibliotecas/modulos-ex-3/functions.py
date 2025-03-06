# Crie um programa modularizado com três funções para calcular a área de três tipos
# de objetos: retângulo, triângulo e círculo.

import math

def area_retangulo(base, altura):
    area = base * altura
    return area

def area_triangulo(base, altura):
    area = (base * altura) / 2
    return f'{area:.2f}'

def area_circulo(raio):
    area = math.pi * (raio ** 2)
    return f'{area:.2f}'
