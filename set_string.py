letras_1 = {'a','c','d','e'}
letras_2 = {'y','j','i','a'}

# União
set_1 = letras_1.union(letras_2)
print(set_1)

# Item Diferente que há entre eles
set_1 = letras_1.difference(letras_2)
print(set_1)

# Item que há de semelhante entre eles
set_1 = letras_1.intersection(letras_2)
print(set_1)