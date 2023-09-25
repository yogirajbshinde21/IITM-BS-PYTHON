a = "yogiraj"
b = 'shinde'
n=a+b
print(n)
# Output : yogirajshinde


a = [22,1,34,55]
b = [23,4,8,54,23]
n=a+b
print(n)
# Output : [22, 1, 34, 55, 23, 4, 8, 54, 23]


n=10+13*2
#my guess is 46 which is mathematically wrong
print(n)
# Output : 36 
# So the correct answer turned out to be 36, that is due to the 'operator precedence'.


n=((10+13)*2)
print (n)
#Output : 46 
#which is the correct answer for this equation.