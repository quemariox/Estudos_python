def imprimir(lista_entrada,lista_saida):
    print('Imprimindo os objetos da lista de entrada')
    while lista_entrada:
        item = lista_entrada.pop()
        lista_saida.append(item)
    print(lista_saida)
    

