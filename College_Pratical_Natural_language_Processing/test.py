def getSecondOrderElements(n: int, a: [int]) -> [int]:
    # Write your code here.
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')
    
    # Traverse the array
    for num in a:
        # Update largest and second largest
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
        
        # Update smallest and second smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    
    # Return the second largest and second smallest
    return [second_largest, second_smallest]

ans = getSecondOrderElements(n = 5,a = [1, 2, 3, 4, 5])
print(ans)