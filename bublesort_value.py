"""
These program invoves in sorting array using  asecding order 
based values of items in a array
    """
    
def bubble_sort(arr):
    """
    these function takes the array as input and 
    returns the array sort array elements based on there value
    """
    for i in range(0,len(arr)):
        for j in range (i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return (arr)

Salary=[1000,2340,5600,4500,3200,1200,500,9000,1800,3700,2500,6700]

print(bubble_sort(Salary))