def encontrar_duplicados(array):  
    elementos_lista=[]
    duplicados=[]

    for elemento in array: 
        if elemento in elementos_lista:  
            duplicados.append(elemento)
        else:  
            elementos_lista.append(elemento) 
    
    return duplicados

print(encontrar_duplicados([1,2,3,4,1,1,2,2,0]))