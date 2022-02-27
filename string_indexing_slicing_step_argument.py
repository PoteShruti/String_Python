'''#string_indexing_slicing_step_argument
# string indexing here we print only one element
name = "shruti"
# indexing always starts with o 
# s = 0         -6
# h = 1         -5
# r = 2         -4
# u = 3         -3
# t = 4         -2
# i = 5         -1(if you want to print last element of name but you dont know the length of string you can use -1 for print the last element)
print(name[0])
print(name[3])
print(name[-1])
print(name[-2]) 
# string slicing - here we print more elements
# syntax - [start argument : stop argument]
print(name[0:2])
print(name[0:]) # whole string will be print 
print(name[2:5])
print(name[:-1])
print(name[:3])
# step argument 
# The step parameter indicates whether numbers should be generated in sequence, or whether some specific integers should be skipped
# syntax : [start argument : stop argument : step]
print(name[0:6:1]) # means we started from 0 and then step 1 means 0 ke baad 1 next no print krneka
print(name[0:6:2]) # here we take step 2 we started from 0 and then step 2 means 0 ke baad 2 no 
# i.e s = 0 , h = 1 , r = 2 , u = 3 , t = 4 , i = 5
# s ke baad ke 2 no i.e r ke baad 2 t 
# srt is answer
# reverse the string
print(name[::-1])
# take name from user and reverse the string
NAME = input("Enter your name :") 
print(f"Reverse of your name is : {NAME[::-1]}") 
# check is it palindrome string or not
if(NAME == NAME[::-1]):
    print("It is a palindrome string!")
else: 
    print("It is not a palindrome string")
'''

#n="shubham "
n=3
arr=list(map(int,input().split()))
print(*arr)    
