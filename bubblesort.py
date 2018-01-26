def bubblesort(arr):
    '''
    Implementation of bubblesort
    
    params: arr is a list of integers
    returns: a sorted list
    
    example: 
    >>>bubblesort([3,2,7,1])
    [1,2,3,7]
    
    Complexity:
    Best case:    O(n)   (input is already sorted)
    Average case: O(n^2) (input is not sorted)
    Worst case:   O(n^2) (input is in reverse order)
    
    '''  
    # Loop till there are zero swaps in a complete pass
    swap = True
    n=len(arr)
    # Make n passes to sort n elements
    for i in range(n):
        if swap == False:
            break
        swap = False #intialize before each pass
        # Last i elements are already sorted
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                #Swap the adjacent elements if they are not in order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
    return arr

if __name__ == '__main__':
    user_input = input('Enter a list of numbers separated by space:\n').strip()
    unsorted = [int(num) for num in user_input.split()]
    print(bubblesort(unsorted))
