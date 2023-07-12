        
nums=[4,5,6,7,0,1,2]
target=0
lo=0
hi = len(nums)-1


while lo<=hi:
    mid = (lo+hi)//2

    if nums[mid]==target:
        print(mid)
            
    if nums[mid]<target:
        hi=mid-1
    else:
        lo=mid+1

    print (-1)