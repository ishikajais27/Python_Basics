def binary_search(a, target):
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2
        
      
        if a[mid] == target:
            return mid
        
        
        elif a[mid] > target:
            high = mid - 1
            
   
        else:
            low = mid + 1

  
    return -1

t = int(input("Enter the item value you wanted to search: "))
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = binary_search(nums, t)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")