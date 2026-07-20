# Lambda é uma função reduzida, que pode ser usada dentro de outra função

def somar(x,y):
    num = lambda x: x * y
    return num(x) + 2 
print(somar(5,5))

def somar(x):
    num = lambda x: x * 2
    return num(x) + 2 
print(somar(5))