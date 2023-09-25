# Accept two positive integers M and N as input
M = int(input())
N = int(input())

# Check if M is less than N
if M < N:
  print(M)
else:
  while M >= N:
    M = M - N
  # Print the final value of M, which is Mk
  if M < N:
    print(M)
