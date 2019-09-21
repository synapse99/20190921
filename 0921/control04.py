Y = ['Jan', 'Feb','Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
Z = ['Annie', 'Betty', 'Claire', 'Daphne', 'Ellie', 'Franchesca', 'Greta', 'Holly', 'Isabel', 'Jenny']

another_dict = {'x':'printer','y':5, 'z':['star', 'circle',9]}
for month in Y:
    print("{!s}".format(month))

for i in range(len(Z)):
    print("{0!s}: {1!s}".format(i, Z[i]))

for j in range (len(Y)):
    if Y[j].startswith('J'):
        print("{}".format(Y[j]))

