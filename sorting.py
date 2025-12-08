
M = [6,7,3,1,89,4,56,32,1,5,7,8,9]

# Selection_sort
def select_sort(L : list[int])->list[int] :
    if len(L) <= 1:
        return L
    length : int = len(L)

    for i in range(length) :
        index : int = i
        for j in range(i,length):
            
            if L[index] > L[j] :
                index = j

        if index != i :

            L[index] , L[i] = L[i] , L[index]      


    return L
print(select_sort(M))  
# bubble_sort
def bubble_sort(L: list[int])->list[int] :
    if len(L) <= 1 :
        return L
    length : int = len(L)

    for i in range(length):
        for j in range(length - 1):
            if L[j] > L[j+1]:
                L[j] , L[j+1] = L[j+1] , L[j]

    return L            

print(bubble_sort(M))  

# quick sort
def quick_sort(L:list[int]) -> list[int] :
    if len(L) <= 1 :
        return L
    length : int = len(L)

    x : int = L[length//2]


    return quick_sort([ value for value in L if value < x]) + [ value for value in L if value == x] +quick_sort([ value for value in L if value > x])


print(quick_sort(M))        


#fusion_sort
def fusion_sort(L:list[int])->list[int]:

    if len(L) <= 1:
        return L
    
    length : int = len(L) // 2

    A = fusion_sort(L[:length])
    B = fusion_sort(L[length:])
    
    i : int = 0 
    j : int = 0 
    k : int = 0
    M = [0]*len(L)
    while i < len(A) and j < len(B) and k < len(L) :

        if A[i] > B[j]:
            M[k] = B[j]
            j += 1

        else:
            M[k] = A[i] 
            i += 1
        k += 1

    while i < len(A) and k < len(L):
            M[k] = A[i]
            k += 1 
            i += 1     

    while j < len(B) and k < len(L):
            M[k] = B[j]
            k += 1 
            j += 1    

    return M
    
          
print("fusion sort is this : ..... ",fusion_sort(M))
    
    






