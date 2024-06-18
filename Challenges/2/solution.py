def make_to_the_end(array):
    farthest_reach = 0
    for i in range(len(array)):
        if i > farthest_reach:
            return False
        farthest_reach = max(farthest_reach, i + array[i])
        if farthest_reach >= len(array) - 1:
            return True
    return farthest_reach >= len(array) - 1


example1 = [1, 3, 1, 2, 0, 1]
example2 = [1, 2, 1, 0, 0]

print(make_to_the_end(example1))  
print(make_to_the_end(example2))  