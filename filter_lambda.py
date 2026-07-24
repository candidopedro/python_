lista = [10,32,57,15]

def remove(x):
    return x > 20

print(list(filter(remove, lista))) # <-- A função 'filter' irá executar primeiro a função 'remove' que retornará valores boolean (false/true) se o item verificado for menor ou maior que 20. Com base nesta nos resultados será impresso no print

print(list(filter(lambda x: x > 20, lista))) # <-- Ao invés de usar a função convencional, usamos a lambda, reduzindo a quantidade de linhas