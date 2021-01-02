#Using reverse() method, only for numerical elements of list

def reverse_num_list(num):
    nums = []
    for i in range(num):
        nums.append(i)
    
    print("\nCurrent List: ", nums)
    nums.reverse()
    print("Reversed List: ", nums)

reverse_num_list(11)

#---------------OR--------------------
#Using reverse() method, only for numerical elements of list

def reverse_num_list(num):
    nums = []
    for i in range(num):
        nums.append(i)
    
    print("\nCurrent List: ", nums)
    print("Reversed List: ", nums[: : -1])

reverse_num_list(11)

#---------------OR--------------------
#Using reverse() method, only for numerical elements of list

def reverse_num_list(num):
    nums = []
    for i in reversed(range(num)):
        nums.append(i)
    print("\nReversed List: ", nums)
    
reverse_num_list(11)


"""
Expected Output

reverse() method
Current List:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Reversed List:  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

Using List slicing
Current List:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Reversed List:  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

reversed() method
Reversed List:  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""
