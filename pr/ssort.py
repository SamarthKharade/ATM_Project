
def sorted_array():
    arr=[]
    n=int(input("Enter the number of elements in the array: "))

    print("Enter the elements of the array:")
    for i in range(n):
        element=int(input())
        arr.append(element)

    print("Unsorted array is :",arr)

    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[min]>arr[j]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]

    return arr


if __name__=="__main__":
    result=sorted_array()
    print("Sorted array is :",result)