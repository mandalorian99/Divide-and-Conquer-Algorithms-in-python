# Quick short algorithm
# family:Divide and conquer
# written by mahendra choudhary
# official website link : www.thecodestuff.com
# email: mahendra@thecodestuff.com

#----funciton used in from------

#quicksort function takes 3 parameters
# array to be sort , lower bound of arry and higher bound of array

def quickSort(arr , low , high):
    #quick sort funtion calls a new function name partion
    #first check value of low is smaller than high
    if low<high :
        #calling partion function 
        pi = partition( arr , low ,high )
        #quickSort(arr ,low ,pi-1)
        #quickSort(arr,pi+1,high)


#defination for partion function
#this function takes 3 value
# arry ,lower value ,higher value 
def partition(arr , low ,high):
    #choosing last value as pivot point
    pivot = arr[high]

    # var i store the index of elements smaller than pivot
    i = (low - 1)
    print("[i][low],[high]-",i,low,high)

    # now traversing the provide array from 0 index
    # we put elements smaller than pivot to left side
    # and elements larger than pivot to right side of pivot
    # var j used to loop through array ,it store index of array
    
    for j in range(low ,high+1):

        if arr[j] <= pivot :
            #increment the index of i
            i=i+1
            print("----------------------")
            print("[loop]for = and i =:",j,i)
            #swap the larger value (index i ) with pivot
            arr[i],arr[j] = arr[j],arr[i]
            print(arr)
            print("------------------------")

    #for last element we increent i for 1 and perform swap
    arr[i+1],arr[j] = arr[j],arr[i+1]
    print("last element sort:",arr)
    return(i+1)
        

#----luncher script----------

# test array

arr=[10,80,80,10,30,90,40,50,70]
low = 0 
high = len(arr)
print("size of array:",high)

#calling a quick sort fucntion
quickSort(arr , low , high-1)

print("----printing sorted array----")
print(arr)
