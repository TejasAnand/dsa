# Define the unsorted array
arr = [10, 5, 1, 1, 2]

# Iterate through each element in the array
for i in range(1, len(arr)):
    # Save the current element
    current = arr[i]
    # Save the index of the element before the current element
    j = i - 1
    # Shift elements to the right until the correct position for the current element is found
    while j >= 0 and arr[j] > current:
        arr[j + 1] = arr[j]
        j -= 1
    # Insert the current element in its correct position
    arr[j + 1] = current

# Print the sorted array
print(arr)
