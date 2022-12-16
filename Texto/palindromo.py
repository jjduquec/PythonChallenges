"""
    Un palindromo es una frase que al leerla 
    al derecho y al reves se lee igual 


    desafio: crear una funcion que determine si 
    una cadena de texto es palindromo 



"""




def palindromo(cadena):
    
    cadena=(cadena.lower()).replace(" ","")
    return cadena == cadena[::-1]
    #[::-1] ->invierte la cadena 
    




print(palindromo("palindromo"))
print(palindromo("Anita LaVa LA TINa"))



