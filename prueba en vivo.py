def run():
    mi_lista = [1, 2, 1, 4, 3, 2, 7, 8, 1, 7]

    # Utilizando una lista auxiliar para encontrar duplicados
    duplicados = []
    unicos = []
    
    for x in mi_lista:
        if x in unicos:
            duplicados.append(x)
        else:
            unicos.append(x)
    
    print("datos duplicados:", duplicados )

if __name__ == '__main__':

    run()

    
    


        


