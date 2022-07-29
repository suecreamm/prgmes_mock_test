from pprint import pprint
from copy import deepcopy

### test set ###
begin_01 = [[0,1,0,0,0],[1,0,1,0,1],[0,1,1,1,0],[1,0,1,1,0],[0,1,0,1,0]]
#target_01 = [[0,1,0,0,0],[1,0,1,0,1],[0,1,1,1,0],[1,0,1,1,0],[0,1,0,1,0]]
target_01 = [[0,0,0,1,1],[0,0,0,0,1],[0,0,1,0,1],[0,0,0,1,0],[0,0,0,0,1]]

begin_02 = [[0,0,0],[0,0,0],[0,0,0]]
target_02 = [[1,0,1],[0,0,0],[0,0,0]]
### test set end ###


m, n = 0, 0                          ### m: lines ### n: columns


### arr에서 x-행, y-열을 뒤집어라 & 몇 번 뒤집었는지 전달해줘라
def invert_arr(arr, x, y, turns):           ### x: lines to invert ### y: columns to invert
    temp_arr = []

    if x == -1:
        temp_arr = arr ### deepcopy
    else:
        for i in range(m):
            if i == x:
                temp_arr.append(list(_ ^ 1 for _ in arr[x]))
            if 0 <= i < m and i != x:
                temp_arr.append(arr[i])
        turns += 1

    temp_arr2 = deepcopy(temp_arr)
    if y == -1:
        pass
    else:
        for _ in range(m):
            temp_arr2[_][y] = temp_arr[_][y]^1
        turns += 1
    return (temp_arr2, turns)


def solution(beginning, target):
    target_inv, target_temp = [], target
    cnt= 0                           ### cnt: 뒤집기 횟수
    global m, n

    if target_temp == begin_01:
        return cnt

    ###### Binary inversion of the target matrix given ###### 반전시킴
    for line in target:
        target_inv.append(list(_ ^ 1 for _ in line))
        m += 1
    n = len(target_inv[0])

    pprint(target_inv)

    ##### ( target_inv 행 뒤집기를 실행 > 그게 beginning이랑 같니? )를 반복

    #while True:
    #if target_temp[0] == beginning:
    #    break
    #if cnt == m+n:
        #return -1
    # 너무 모르겠음
    for i in range(m):
        for j in range(n):
            print(i, j)
            target_loop = invert_arr(target_inv, i, j, cnt)
            cnt += 1
            #target_loop = invert_arr(target_inv, )
            if target_loop[0] == beginning:
                pprint(target_loop[0])
                print(target_loop[-1])
            else:
                target_loop = invert_arr(target_inv, i+1, j, cnt)

    pprint(target_loop[0])

    return target_temp


solution(begin_01, target_01)
