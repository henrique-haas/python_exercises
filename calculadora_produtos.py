preço = float(input('Digte o preço do produto(R$): '))
print('[1] À vista com dinheiro ou cheque: 10% de desconto')
print('[2] À vista no cartão: 5% de desconto')
print('[3] Até 2x no cartão: Preço normal')
print('[4] Em 3x ou mais no cartão: 20% de juros')
pagamento = int(input('Digite o número da condição de pagamento: '))

if pagamento == 1:
    print(f'O preço do produto é de R${preço:.2f} e o valor final será de R${preço - (preço*0.10):.2f}')
elif pagamento == 2:
    print(f'O preço do produto é de R${preço:.2f} e o valor final será de R${preço - (preço*0.05):.2f}')
elif pagamento == 3:
    parcela = preço / 2
    print(f'O valor final do produto será de R${preço:.2f}, em duas parcelas de R${parcela:.2f}.')
elif pagamento == 4:
    qtdparcelas = int(input('Quantas parcelas? '))
    parcela = preço / qtdparcelas
    juros = preço + (preço*0.20)
    print(f'O preço do produto é de R${preço:.2f} e o valor final será de R${juros:.2f} em {qtdparcelas} parcelas de R${juros / qtdparcelas:.2f}')
else:
    print('Digite uma opção válida!')


