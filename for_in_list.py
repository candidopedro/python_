veiculos = ['BYD Seal', 'Fiat Pulse', 'BYD Song Plus', 'Ford Maverik']
veiculos_byd = []

for item in veiculos:
    if 'BYD' in item:
        veiculos_byd.append(item)

print(veiculos_byd)

veiculos_byd2 = [item.upper() for item in veiculos if 'BYD' in item] # <-- Foi usado um 'for' dentro da lista / 'item.upper()' é um exemplo para mostrar que alterando aquele 'item', os itens atribuidos a lista serão alterados
print(veiculos_byd2)
