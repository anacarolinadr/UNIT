# Implemente um arquivo chamado funções.py com duas funções: uma
# para ver se o número é par ou impar e outra para calcular a média
# entre dois números.

# Na sequencia crie um arquivo programa.py que implemente o uso
# dessas duas funções.

def impar_par(num):
    if (num % 2) == 0:
        return "Número par"
    else:
        return "Número ímpar"
    
def media(num1, num2):
    return f'Média: {((num1 + num2) / 2 ):.2f}'