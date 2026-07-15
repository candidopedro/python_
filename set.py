list_1 = [1,4,7]
list_2 = [2,4,8]

num1 = set(list_1)
num2 = set(list_2)

print(num1 | num2) # Juntar
print(num1 - num2) # Remover duplicados
print(num1 ^ num2) # Deixar apenas os diferentes
print(num1 & num2) # Mostar apenas os duplicados