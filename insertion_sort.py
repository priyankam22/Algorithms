def insertion_sort(arr):
    '''
    
    Implementation of insertion sort
    
    params: arr is a list of numbers
    returns: a sorted list
    
    example: 
    >>>insertion_sort([3,2,7,1])
    [1,2,3,7]
    
    Complexity:
    Best case:    O(n)   (input is already sorted)
    Average case: O(n^2) (input is not sorted)
    Worst case:   O(n^2) (input is in reverse order)
    
    '''
    n = len(arr)
    
    for i in range(1,n):
        while i > 0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i-=1
    return arr


if __name__ == '__main__':
    user_input = input('Enter a list of numbers separated by space:\n').strip()
    unsorted = [int(num) for num in user_input.split()]
    print(insertion_sort(unsorted))