root_node = [1, 2, 3, 4, 5]           # 모두 이용해서 줄세우기, 선택만 하면 되기 때문에 중복을 빼야함
combi_result = []


def dfs(d, l, cnt):
    global root_node
    global combi_result

    if cnt == 3:                # cnt ==
        combi_result.append(d)
        return combi_result
    for i in l:
        down = d[:]
        down.append(i)
        l1 = l[:]
        l1.remove(i)
        for j in range(i):
            try: l1.remove(j)
            except ValueError: continue
        print(down, l1)
        dfs(down, l1, cnt+1)
    return combi_result


print(dfs([], root_node, 0))
print(len(combi_result))
