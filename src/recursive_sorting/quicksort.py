# [5 9 3 7 2 8 1 6]

# [3 2 1] [5] [9 7 8 6]

my_list = [ 5, 9, 3, 7, 2, 8, 1, 5]

# print(5 in my_list)

# def is_it_in_here(n):
#     for item in my_list:
#         if item == n: 
#             return True
#     else:
#         return False

def partition(data):
    left = []
    pivot = data[0]
    right = []
    

    for item in data[1:]:
        if item < pivot:
            left.append(item)
        else: #Hanling > or =
            right.append(item)
    
    return left, pivot, right

print()