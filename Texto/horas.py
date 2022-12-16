"""
funcion que reciba una cadena con el siguiente formato : 

Horas:Minutos AM/PM 

Retorna :  

Horas:Minutos  


"""

#solucion planteada:  
def formato(horario):
    #separamos la cadena  
    horario=horario.split() 
    hora=int(horario[0][:2]) 
    minutos=horario[0][3:5]
    #verificamos si estan en AM O PM 
    if horario[1].upper()=='PM' and hora <12 : 
        #estamos antes de media noche 
        hora+=12
    elif hora==12:  
        #estamos a media noche 
        hora="00"
    
    return str(hora)+":"+minutos




print(formato("04:59 PM"))

        

