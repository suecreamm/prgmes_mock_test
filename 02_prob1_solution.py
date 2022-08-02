num01 = [-2, 3, 0, 2, -5]
num02 = [-3, -2, -1, 0, 1, 2, 3]
num03 = [-1, 1, -1, 1]

root_node = []
combi_result = []


def combi(d, l, cnt):
    global root_node
    global combi_result

    if cnt == 3:                # cnt ==
        combi_result.append(d)
        return combi_result
    for i in l:
        ind = l.index(i)
        down = d[:]
        down.append(i)
        l1 = l[:]
        l1.remove(i)
        for j in range(ind):
            try: l1.remove(l[j])
            except ValueError: continue
        combi(down, l1, cnt+1)
    return combi_result


def solution(number):
    global root_node
    global combi_result
    root_node = deepcopy(number)
    combi([], root_node, 0)
    result = 0

    for i in range(len(combi_result)):
        if sum(combi_result[i]) == 0:
            print(combi_result[i])
            result += 1
        else:
            continue
    
    if result > 0:
        return result
    else:
        return -1






"""
print(solution(num01))
ans: 2

print(solution(num02))
ans: 5

print(solution(num02))
ans: -1
"""
