#Implementation of binary search algorithm using python
#binary search is divide and conqueor algorithm
#It is used to search a element from a sorted array

#defination of binary search function
def binarySearch(arr,low,high,x):
    if low<=high:
        #finding mid index of array
        mid=int( (low+high)/2  )

        #checking if the x is itself at middle or not
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            #if x is greter than mid element
            #then return mid+1 index and ignore the left elements
            #calling binary serach funciton again
            return binarySearch(arr,low,mid-1,x)
        else:
            return binarySearch(arr,mid+1,high,x)
    else:
        return -1
#function defination end

#launcher script
arr=[10,12,14,19,45,50,55,56,59,60,39]
size=len(arr)-1
print(size)
#we have search for x
x=59
#function call
result = binarySearch(arr,0,size,x)

if result != -1:
    print("Element x is present at index %d",result)
else:
    print("Element is not present in the list")
