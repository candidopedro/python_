num = {1,7,9}
# Adicionar
num.add(5)
print(f'{num}')

# Adicionar e não duplicar
num.update(7)
print(f'{num}')

# Removendo - se não for encontrado o item, um erro será gerado
num.remove(9)
print(f'{num}')

# Removendo - se não for encontrado o item, será ignorado
num.discard(8)
print(f'{num}')