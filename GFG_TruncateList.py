#Method 1:
def clearList(my_list):
    print("Given List before truncating is: ", my_list)
    my_list.clear()
    print("Given List after truncating is: ", my_list)
    
clearList([1,2,3,4,5])

#Method 2:
def clearList2(my_list2):
    print("Given List before truncating is: ", my_list2)
    my_list2 *= 0
    print("Given List after truncating is: ", my_list2)

clearList2([1,2,3,4,5,6,7,8,9,10])

#Method 3:
def clearList3(my_list3):
    print("Given List before truncating is: ", my_list3)
    del my_list3[:]
    print("Given List after truncating is: ", my_list3)

clearList3([1,2,3,4,"Hello", True])

#Method 4:

def clearList4(my_list4):
    print("Given List before truncating is: ", my_list4)
    my_list4 = []
    print("Given List after truncating is: ", my_list4)

clearList4([1,2,3,4,])

'''
Expected output:
Given List before truncating is:  [1, 2, 3, 4, 5]
Given List after truncating is:  []
Given List before truncating is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Given List after truncating is:  []
Given List before truncating is:  [1, 2, 3, 4, 'Hello', True]
Given List after truncating is:  []
Given List before truncating is:  [1, 2, 3, 4]
Given List after truncating is:  []
'''
