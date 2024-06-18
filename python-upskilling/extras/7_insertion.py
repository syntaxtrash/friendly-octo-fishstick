def insertion_sort(array):

    for current_index in range(1, len(array)):
        key = array[current_index]
        
        # Move elements of the sorted part of the array that are greater than key, to one position ahead
        previous_index = current_index - 1
        while previous_index >= 0 and key < array[previous_index]:
            array[previous_index + 1] = array[previous_index]
            previous_index -= 1
        
        # Insert the key into its correct position in the sorted part of the array
        array[previous_index + 1] = key
    
    return array

arr = [64, 25, 12, 22, 11]
sorted_arr = insertion_sort(arr.copy())

print("Original array:", arr)
print("Sorted array:", sorted_arr)
