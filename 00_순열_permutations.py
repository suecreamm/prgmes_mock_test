from copy import deepcopy

root_node = [1, 2, 3]           # 모두 이용해서 줄세우기
permu_result = []


def dfs(d, l, cnt):
    global root_node
    global permu_result

    if cnt == len(root_node):
        permu_result.append(d)
        return permu_result
    for i in l:
        down = d[:]
        down.append(i)
        l1 = deepcopy(l)            # 혹은 l1 = l[:]
        l1.remove(i)
        dfs(down, l1, cnt+1)
    return


dfs([], root_node, 0)
print(permu_result)
