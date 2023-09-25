a = input()       # Read the input string

# Read the start and end indices
b = int(input())
c = int(input())

# Extract the specified substring
substring = a[b:c+1]

# Calculate the minimum number of repetitions needed
repetition = (len(a)+1) // len(substring)

# Create the new string by repeating the substring
newstring = substring * repetition

# Print the new string
print(newstring)