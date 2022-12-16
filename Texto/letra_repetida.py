
"""
encontrar la primera letra repetida en una frase o palabra


"""
def repetida(texto):
    texto=(texto.lower()).replace(" ","") 
    lista_letras=[]
    for char in texto: 
        if char in lista_letras:  
            return char  
        else:
            lista_letras.append(char)

    return None 



print(repetida("HolA"))
print(repetida("hola mundo"))