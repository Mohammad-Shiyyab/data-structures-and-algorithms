import math

def BinarySearch(arr,key):
    a=0
    b=len(arr) -1
    while a<= b :
        mid = mid = math.ceil((a + b ) /2)
        if (a + b ) /2 < 1:
            mid = math.floor((a + b ) /2)
        
        if arr[ mid ] ==key:

            return mid
        elif a == b:
            return -1     
        elif arr[ mid ] <key:
            a= mid 
            
        else:
            b=mid 


arr=[1, 3, 5,7, 11, 13, 17,19,23,29,31,37,41,43,47,53,59]
key=  -1

print(BinarySearch(arr,key))