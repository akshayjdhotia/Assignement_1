def isValidSubSequence(array,sequence):
    index_values =[]
    for i in array:#O(n)
        if i in sequence:
            index_values.append(sequence.index(i))
    index_values_sorted = sorted(index_values) #O(nlog2n)(TimSort)
    return index_values_sorted == index_values



if __name__ == "__main__":
    sample_array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    if (isValidSubSequence(sample_array, sequence)):
        print("True")
    else:
        print("False")

# Time Complexity O(n)
# Space Complexity O(n)

# Test cases
# 1)
#     sample_array = [5, 1, 22, 25, 6, -1, 8, 10]
#     sequence = [1, 6, -1, 10]
# output true (Expected)

# 2)
#     sample_array = [5, 6, 22, 25, 1, -1, 8, 10]
#     sequence = [1, 6, -1, 10]
# output False(Expected)

