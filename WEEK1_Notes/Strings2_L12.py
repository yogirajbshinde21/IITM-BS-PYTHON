#################################################

s = 'good'
print(s * 5)
#Output : goodgoodgoodgoodgood

#################################################

print(s[0] * 5)
#Output : ggggg

#################################################

#String comparison 1:
x = 'India'
print(x == 'India')  #Output : True
print(x == 'india')  #Output : False

##################################################

#String comparison 2:

print('apple' > 'one')  # False, because 'a' comes before 'o' in the alphabet.

print('four' < 'ten')  # True, because 'f' comes before 't' in the alphabet.

print(
    'ab' > 'az'
)  # False, because the first letter in both are the same but they differ in the second letters as per the alphabetical order.

####################################################

# NEGATIVE INDEXING:

#Is it even possible to access negative index for a string?
#Yes, it is possible.
s = 'python'
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print(s[-6])
#It will gives the string in reverse order.

###################################################

#TO FIND THE LENGTH OF THE STRING :

s = 'sjhvfehvbdfmnvbefgvdbfvkjdfvhefvjdjvhkdcjhevhedvbkejdvkdjbv,djbvkevkedfv,kndvhldhvdnvdshvkdshv'

print(len(s))  #Output : 94


print(s[94])  #Error, because Python String indexing starts from 0.
