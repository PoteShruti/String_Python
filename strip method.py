#strip method
# used for remove the spaces
name = '      shruti      '
dots = '..........' 
print(name) 
print(name + dots)
#lstrip method remvoes the spaces of left side
print(name.lstrip()+dots)
#rstrip method removes the spaces of right side
print(name.rstrip()+dots)
# strip method it removes left as well as right spaces
print(name.strip()+dots)
# if the spaces in the middle we cant use strip method then we will use replace method
nam = '   chu    dail  '
# here we will replace space with *
print(nam.replace(" ","*"))
# here we replace space with no space
print(nam.replace(" ",""))