def bubble_sort(array): 
    changes=True
    size=len(array)-1
    while(changes):  
        changes=False 
        for i in range(size): 
            if array[i]>array[i+1]:  
                changes=True 
                aux=array[i] 
                array[i]=array[i+1]
                array[i+1]=aux  
    return array 





print(bubble_sort([6,5,3,1,8,7,2,4]))