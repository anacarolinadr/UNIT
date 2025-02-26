# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma
# prestação de uma conta.

# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar
# estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor
# ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela.

# Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até
# que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser
# encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas
# no dia.

# O cálculo do valor a ser pago é feito da seguinte forma: para pagamentos sem atraso, cobrar o valor
# da prestação; quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

# Mesmo caso do exercício anterior - não havia motivo para utilizar POO

def valorPagamento(vl, dias):
    if dias == 0:
        return vl
    else:
        vljuros = dias * (0.001 * vl)
        vlmulta = vl * 0.03
        return vl + vljuros + vlmulta

total_prestacoes = 0
valor_total = 0

while True:
    pagto = float(input('Valor do pagamento: '))
    if pagto == 0:
        break
    
    diasAtraso = int(input('Dias de atraso: '))
    valorFinal = valorPagamento(pagto, diasAtraso)
    
    print(f'\nValor a ser pago: R$ {valorFinal:.2f}\n')
    
    total_prestacoes += 1
    valor_total += valorFinal

print('\nRelatório do dia:')
print(f'Quantidade de prestações pagas: {total_prestacoes}')
print(f'Valor total das prestações: R$ {valor_total:.2f}')