

def aplanar_lista(array): 
    
    for i in range(len(array)): 
        if isinstance(array[i], list):  
            for x in array[i]: 
                array.append(x)

            array.pop(i) 

    return array  

#solucion propuesta  

def aplanarlista(array):  
    nueva_lista=[] 
    for elemento in array: 
        if type(elemento) is list :  
            nueva_lista.extend(elemento)
        else:  
            nueva_lista.append(elemento)
    return nueva_lista


print(aplanarlista([2,3,4,[[2]]]))


    


