""" This is for copying example """

# a = [1, 2, 3]
# b = a
#
# print (a)
# print (b)
# print (a is b)
#
# b[0] = 300
# print (a)
# print (b)
# print (a is b)

# a = [1,2,3]
# b = a[::]
# print (a)
# print (b)
# print (id(a))
# print (id(b))
# print (a is b)
# print (a == b)  # address of a is equal to address of b

a = [1, 2, 3, [20, 40]]
b = a[::] # a[:]
print (a)
print (b)
print (a is b)
print (a[3] is b[3])
b[3][0] = 400
print (a)