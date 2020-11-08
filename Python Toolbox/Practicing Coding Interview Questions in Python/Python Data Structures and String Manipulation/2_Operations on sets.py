A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 7, 9, 11, 13, 15}
C = {1, 2, 8, 10, 11, 12, 13, 14, 15, 16, 17}
D = {1, 3, 5, 7, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
E = {9, 10, 11, 12, 13, 14, 15}


intx = B.intersection(C)

unio = A.union(intx)

intx2 = D.intersection(E)

result = unio.difference(intx2)

print(result)
