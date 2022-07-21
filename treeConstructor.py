# Python_tree_constructor (verifier) --> CODERBYTE

'''
TreeConstructor(strArr) take the array of strings stored in strArr, 
which will contain pairs of integers in the following format: (i1,i2), 
where i1 is child node and i2 represents the parent node.

If strArr can form a proper binary tree, return True. If not, return False

            4
           /
          2
        /   \
      1       7

Example 1
Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"] 
Output: true
Example 2
Input: ["(1,2)", "(3,2)", "(2,12)", "(5,2)"] 
Output: false


# my_notes:
# (left, right) --> left is the child, and right is the parent of the child
'''


s = ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]
childList = []
parentList = []


def TreeConstructor(s):
    for each in s:
        childList.append(each[1])
        parentList.append(each[3])
    # print(childList)
    # print(parentList)

    countList = dict((x,parentList.count(x)) for x in set(parentList))
    # print(countList)
    # print(list(countList.values()))

    if max(list(countList.values())) >2:
        print('FALSE')
        return False
    else:
        print('TRUE')
        return True


TreeConstructor(s)
