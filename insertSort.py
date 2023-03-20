infoList = [5, 2, 8, 4, 9, 3, 6]

# 创建一个新的空列表
List = []

# 遍历原列表的每个元素
for i in infoList:
    if len(List) == 0:
        List.append(i)
    else:
        for j in range(len(List)):
            if i <= List[j]:
                List.insert(j, i)
                break
            elif j == len(List) - 1:
                List.append(i)
                break

# 打印排序后的列表
print(List)
