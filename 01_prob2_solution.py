from collections import Counter

# A = ["banana", "apple", "rice", "pork", "pot"]
# B = [3, 2, 2, 2, 1]
# C = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]


def solution(want, number, discount):
    W = {}
    ##### Counter를 collections import하고 쓰는 걸 기억 자체를 못했음

    for i in range(len(A)):         ###### 원하는 item 개수 dict로 만들기
        W[want[i]] = number[i]

    D = Counter(discount)
    print(D)
    cnt = 0

    for _ in list(W.keys()):
        if W[_] <= D[_]:
            cnt += 1
        if _ not in D:
            return 0
        else:
            continue

    if cnt < len(W.keys()):
        return 0

    cnt = 0
    left, right = 0, 9

    while cnt <= len(W.keys()):
        if cnt == len(W.keys()):
            break

        for _ in list(W.keys()):
            temp_D = Counter(discount[left:right + 1])
            if W[_] == temp_D[_]:
                cnt += 1
            if (_ not in temp_D) or (W[_] < temp_D[_]):
                left += 1
                right += 1
    return left+1
    ###### left였는지 left+1이었는지 기억이 안남

#print(solution(A, B, C))
