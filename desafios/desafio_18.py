cars = ['BMWX6', 'BMWI5', 'BMWI8']
car = input('Digite o carro que deseja: ')

if car.upper().replace(' ', '') in cars:
    print(f' - {car.upper().replace('W', 'W ')} está disponivel para compra')
else:
    print(f'- {car.upper().replace('W', 'W ')} indisponivel para compra')        