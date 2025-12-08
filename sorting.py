
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



# quick sort
def quick_sort(L:list[int]) -> list[int] :
    if len(L) <= 1 :
        return L
    length : int = len(L)

    x : int = L[length//2]


    return quick_sort([ value for value in L if value < x]) + [ value for value in L if value == x] +quick_sort([ value for value in L if value > x])


print(quick_sort(M))        





