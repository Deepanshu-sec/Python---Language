#     *
#   * * *
# * * * * *
#   * * *
#     *
n = int(input("Enter a number : "))

for i in range(1,n+1):
    print("  "* (n-i),end = " ")
    print("* "* (2*i-1),end = " ")
    print()
for j in range(n,1,-1):
    print("  "* (n+1-j),end=" ")
    print("* "* (2*j-3),end=" ")
    print()
    