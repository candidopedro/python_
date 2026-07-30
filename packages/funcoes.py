def busca(lista_numerica, item_busca):
    for item in lista_numerica:
        if lista_numerica[item] == item_busca:
            localizacao = lista_numerica.index(item_busca)
            print(f'O item foi localizado no index [{localizacao-1}]')

# Index está saindo igual ao item_busca