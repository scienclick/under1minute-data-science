# <editor-fold desc="#1- list operations">
sample_list_1 = [1, 2, 2, 3, 4, 5, 6, 7]
sample_list_2 = ["a", "b"]

'''----------------------------------length of a list'''
len(sample_list_1)

'''----------------------------------reversing a list'''
sample_list_2.reverse()
sample_list_2

'''----------------------------------counting an element'''
sample_list_1.count(2)

'''----------------------------------extending list'''

sample_list_1 + sample_list_2  # attaches two lists together

sample_list_1 += [-1, -10]  # appends [-1,-10] to the end of the list
sample_list_1
sample_list_1.extend(sample_list_2)  # attaches two lists together
sample_list_1
sample_list_1.append(-2)  # appends [0] to the end of the list
sample_list_1
sample_list_1.insert(1, -2)  # inserts -2 at index 1
sample_list_1

'''----------------------------------index of an element'''
sample_list_1.index(-2)

'''----------------------------------removing elements from a list'''
sample_list_1.remove(-2)
sample_list_1

# </editor-fold>


# <editor-fold desc="#2- list operation examples">
sample_list_1 = [1, 2, 2, 3, 4, 5, 6, 7,-100,-100]
exclusion_list = [4,5]
'''----------------------------------list comprehension examples'''

[element for element in sample_list_1 if element  not in exclusion_list] #list with no 4,5

[element for element in sample_list_1 if element != 2] #list with no 2 in it

[index for index, element in enumerate(sample_list_1) if element == -100] #index of element 2


# </editor-fold>