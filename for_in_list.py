veiculos = ['BYD Seal', 'Fiat Pulse', 'BYD Song Plus', 'Ford Maverik']
veiculos_byd = []

for item in veiculos:
    if 'BYD' in item:
        veiculos_byd.append(item)

print(veiculos_byd)

veiculos_byd2 = [item for item in veiculos if 'BYD' in item] # <-- Foi usado um 'for' dentro da lista
print(veiculos_byd2)
