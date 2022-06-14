
# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}


a="w3resource"
# i=0
# d={}
# while i<len(a):
#     j=0
#     c=0
#     while j<len(a):
#         if a[i]==a[j]:
#             c=c+1
#         j=j+1
#     d.update({a[i]:c})
#     i=i+1
# print(d)
d={}
for i in a:
    c=0
    for j in a:
        if i==j:
            c=c+1
    d.update({i:c})
print(d)
