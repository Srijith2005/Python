print("Hello world")
print("hii")
#Time complexity - O(1)

l=[1,2,3,4,5]
for i in l:
    print(i)
#Time complexity - O(n)

l=[2,3,4,5] #bestcase O(n),n=1
a=2
for i in l:
    if i==a:
        print("True")
l=[1,3,2,4,5] #Averagecase O(n),n=3
a=2
for i in l:
    if i==a:
        print("True")
l=[5,4,3,2] #Worstcase O(n),n=4
a=2
for i in l:
    if i==a:
        print("True")


Binary search
#Time complexity - O(log N)Lograthmic

Merge sort
#Time complexity - O(NlogN)Linear Lograthmic

l=[1,2,3,4,5]
for i in l:
    for j in l:
        print (i,j)
#Time complexity - O(N^2)Quadratic