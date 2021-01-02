#Using reverse() method, only for numerical elements of list
def reverse_num_list(num):
    nums = []
    for i in range(num):
        nums.append(i)
    
    print("\nCurrent List: ", nums)
    nums.reverse()
    print("Reversed List: ", nums)

reverse_num_list(11)


"""
Expected Output
Current List:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Reversed List:  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""
