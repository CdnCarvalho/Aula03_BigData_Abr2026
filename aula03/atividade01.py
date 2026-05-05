valor_compra = float(input('Informe o valor: '))
if valor > 250:
    desconto = valor_compra * 0.16
    valor_final = valor_compra - desconto
    print(f'Valor com desconto de 16% R$ {valor_final}')
else:
    print(f'Valor sem desconto: R$ {valor_compra}')