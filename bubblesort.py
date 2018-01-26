
# coding: utf-8

# ## Bubble sort
# 
# First try

# In[15]:


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
    swap = True
    
    # Loop till there are zero swaps in a complete pass
    while swap:
        swap = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                #Swap the adjacent elements if they are not in order
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
    return arr

if __name__ == '__main__':
    user_input = input('Enter a list of numbers separated by space:\n').strip()
    unsorted = [int(num) for num in user_input.split()]
    print(bubblesort(unsorted))

