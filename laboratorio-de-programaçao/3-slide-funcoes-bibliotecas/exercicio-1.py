# Faça um programa que converta da notação de 24 horas para a
# notação de 12 horas. Por exemplo, o programa deve converter 14:25 em
# 2:25 P.M. A entrada é dada em dois inteiros.

# Deve haver pelo menos duas funções: uma para fazer a conversão e
# uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’
# para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões
# terá um parâmetro formal para registrar se é A.M. ou P.M.

# Inclua um loop que permita que o usuário repita esse cálculo para
# novos valores de entrada todas as vezes que desejar.

import datetime

def conversao_horas(horario):
    hora = horario // 100
    minuto = horario % 100   
    tempo = datetime.datetime(2024, 1, 1, hora, minuto)

    return tempo.strftime("%I:%M"), tempo.strftime("%p")[0]

def formatar_saida(hora_formatada, periodo):
    return f"\n{hora_formatada} {periodo}.M."

while True:
    
    horario = input("Digite o horário (ex: 14:25): ")
        
    try:
        horario = int(horario.replace(':', ''))
        hora = horario // 100
        minuto = horario % 100
        
        if 0 <= hora <= 23 and 0 <= minuto <= 59:
            hora_conv, periodo = conversao_horas(horario)
            print(formatar_saida(hora_conv, periodo))
        else:
            print("Horário inválido! O formato correto é 00:00")
        
        if input("\nDeseja continuar? (S/N): ").upper() != 'S':
            break
            
    except ValueError:
        print("Por favor, digite apenas números!")  