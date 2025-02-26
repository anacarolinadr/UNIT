# Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do
# usuário e imprima a data com o nome do mês por extenso. O
# programa deve chamar uma função que retorna o mês convertido.
# Exemplo:
# – Entrada - Data de Nascimento: 29/10/1973
# – Saída - Você nasceu em 29 de Outubro de 1973.

import datetime

def data_convertida(data):
    ano, mes, dia = data
    
    data_obj = datetime.datetime(ano, mes, dia)
    
    meses = {
        1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
        5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
        9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
    }
    
    return f"Você nasceu em {dia} de {meses[mes]} de {ano}."


data_input = input("Digite sua data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = map(int, data_input.split('/'))
print(data_convertida((ano, mes, dia)))

