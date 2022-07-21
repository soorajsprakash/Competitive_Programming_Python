# FizzBuzz --> LEETCODE

'''
Given an integer n, return a string array answer (1-indexed) where:
    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
'''
  

def fizzBuzz():
    list = []
    n = int(input("enter n: "))
    for each in range(1, n+1):
        if each % 3 == 0 and each % 5 ==0:
            list.append("FizzBuzz")
        elif each% 5 ==0:
            list.append("Buzz")
        elif each % 3 ==0:
            list.append("Fizz")
        else:
            list.append(str(each))
    print(list)
    return list

fizzBuzz()

