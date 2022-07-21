# Bitmap_Holes --> CODERBYTE

'''
Have the function BitmapHoles(strArr) take the array of strings stored in strArr, 
which will be a 2D matrix of 0 and 1's, and determine how many holes, 
or contiguous regions of 0's, exist in the matrix. 
A contiguous region is one where there is a connected group of 0's going in 
one or more of four directions: up, down, left, or right. 
For example: if strArr is ["10111", "10101", "11101", "11111"], 
then this looks like the following matrix:

1 0 1 1 1
1 0 1 0 1
1 1 1 0 1
1 1 1 1 1

For the input above, your program should return 2 because there are 
two separate contiguous regions of 0's, which create "holes" in the matrix. 
You can assume the input will not be empty. 

Example1:
Input: ["01111", "01101", "00011", "11110"]
Output: 3

Example2
Input: ["1011", "0010"]
Output: 2 
'''


count = 0
def BitmapHoles(strArr):
    newList = []
    
    def horizontalCount(ourList):  
        global count
        for each in ourList:
            z = list(each)
            index = 0
            while index < len(z)-1:
                if z[index] == '0' and z[index+1] == '0':
                    count += 1
                    break
                index +=1

    def transpose():
        newStr = ""
        i = 0
        while i < len(strArr[0]):
            for each in strArr:
                newStr += each[i]
            # print(newStr)
            newList.append(newStr)
            newStr = ""
            i += 1

    # print(f"Sample1: {strArr}")
    horizontalCount(strArr)
    # print(f"Initial count: {count}")
    transpose()
    # print(f"Transposed Sample: {newList}")
    horizontalCount(newList)
    # print(f"Final count: {count}")
    return count

print(BitmapHoles(["01111", "01101", "00011", "11110"]))
