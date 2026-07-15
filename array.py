# Para melhorar o desempenho quando houver listas muito extensas
import array

cars = ['golf','rs3','TT']

cars_arrys = array.array('u',['golf','rs3','TT']) # Onde está a letra 'U' é onde se define o tipo de variável

print(f'{cars_arrys}')