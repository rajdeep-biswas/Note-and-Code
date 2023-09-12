def rotate_and_convert(arr):

    # most rudimentary version of Ikir Mikir by ChatGPT. take array of 1s and flip every 5th element into a 0, not counting any element that has been flipped into a 0 from a previous iteration
    target_occurrence = 5
    while arr.count(1) > 1:
        count = 0
        index = 0

        while count < target_occurrence - 1:  # Convert the target_occurrence - 1 occurrence
            if arr[index] == 1:
                count += 1
            index = (index + 1) % len(arr)

        while arr[index] != 1:
            index = (index + 1) % len(arr)

        arr[index] = 0

    return arr

# Example usage:
initial_array = [1, 1, 1, 1, 1, 1, 1]
final_array = rotate_and_convert(initial_array)
print(final_array)
