def selection_sort(array):
    length = len(array)
    
    for current_index in range(length):
        min_index = current_index
        
        # Find the index of the smallest element in the remaining unsorted part
        for j in range(current_index + 1, length):
            if array[j] < array[min_index]:
                min_index = j
        
        # Swap the current element with the smallest element found
        temp = array[min_index]
        array[min_index] = array[current_index]
        array[current_index] = temp
    
    return array

original_array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(original_array.copy())

print("Original array:", original_array)
print("Sorted array:", sorted_array)
