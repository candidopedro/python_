# Usando o While
# Preço deverá cair a cada dia, porém não dever ser menor que 25 reais

value = 100
day = 1

print('--- Promoção enquanto os estoques durarem! ---')
while value > 25: 
    print(f'{day}° dia!')
    print(f'Valor do Produto: R${value} \n')
    day += 1
    value -= 5