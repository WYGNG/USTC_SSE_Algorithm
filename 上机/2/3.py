#输入行数
rows = eval(input("Enter the number of rows in the mat: "))
#输入行
mat = []
for i in range(rows):#按行循环
    items = input("Enter a row: ").strip().split()#对输入的串去除空格并切片
    mat.append([ eval(x) for x in items ]) #字符类型转换成数值并排成列表,附到矩阵mat上

#mat = [[1,4,8,0,8],[3,0,4,5,6],[4,5,6,7,8],[4,3,6,8,9],[3,4,7,5,2]]
is_c = False
r = len(mat)
c = len(mat[0])
for i in range(r):
    # 通过对0元素把对应行和列首个元素置零来减少空间复杂度和时间复杂度
    # 当mat[0][0]被置0需要一个额外的变量区分行和列需要置0.
    # 使用 mat[0][0] 代表第一行.
    if mat[i][0] == 0:
        is_c = True
    for j in range(1, c):
    # 如果这一行有0元素,把对应行和列首个元素置零
        if mat[i][j]  == 0:
            mat[0][j] = 0
            mat[i][0] = 0

# 再次遍历矩阵，对该置0的行与列置0
for i in range(1, r):
    for j in range(1, c):
        if not mat[i][0] or not mat[0][j]:
            mat[i][j] = 0

# 如果第一行需要置0再进行操作
if mat[0][0] == 0:
    for j in range(c):
        mat[0][j] = 0

# 如果第一列需要置0再进行操作        
if is_c:
    for i in range(r):
        mat[i][0] = 0

print(mat)