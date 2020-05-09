#binary search
def binarySearch(listItems,searchItem):
    low=0
    high=len(listItems)-1
    
    while(low<=high):
        mid=(low+high)/2
        
        if(listItems[mid]==searchItem):
            return mid
        elif(listItems[mid]<searchItem):
            low=mid+1
        else:
            high=mid-1
    return None
    
listItems = [1,3,5,7,9,11,13,15,17]
print binarySearch(listItems,3)
print binarySearch(listItems,2)
print binarySearch(listItems,4)
print binarySearch(listItems,5)
print binarySearch(listItems,17)
print binarySearch(listItems,15)