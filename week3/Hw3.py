a = [[1,2,4], [3,5,7], [2,4,9]]
b = [[None]*3 for row in range(3)]

for i in range(3):
    for j in range(3):
        b[i][j] = a[j][i]

print("A矩陣轉置後為:")
for i in range(3):
    for j in range(3):
        print(b[i][j],end='\t')
    print("")