from collections import Counter

# A = ["banana", "apple", "rice", "pork", "pot"]
# B = [3, 2, 2, 2, 1]
# C = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]


def solution(want, number, discount):
    W = {} # want에 있는 item 종류, 개수 담을 공간
    ##### Counter를 collections import하고 쓰는 걸 기억 자체를 못했음

    for i in range(len(A)):         ###### 원하는 item 개수 dict로 만들기
        W[want[i]] = number[i]

    D = Counter(discount)           ###### discount list 전체에 있는 아이템, 개수  

    cnt = 0                         ###### 날짜 바꿔가면서(temp_D) 아이템, 개수가 want와 일치하는지 아닌지 판단함

    for _ in list(W.keys()):
        if W[_] <= D[_]:            ###### D에서 아이템 종류, 수량 만족하면 cnt = len(want)가 됨
            cnt += 1
        if _ not in D:              ##### want에서 원하는 item이 D에 없다면 바로 return 0
            return 0
        else:                       ##### 아무것도 아니면 일단 다음 아이템 살펴보기
            continue

    if cnt < len(W.keys()):         ##### 원하는 아이템 종류가 부족하면 return 0
        return 0

    cnt = 0                         ##### Initializing cnt 
    left, right = 0, 9              ##### 원하는 아이템은 10개로 고정되어 있기 때문에, 아이템 0개의 인덱스를 정한다. 연속되어 있기 때문에 처음 꺼 0, 마지막 9 -> total 10개

    while cnt <= len(W.keys()):
        if cnt == len(W.keys()):    ##### 원하는 아이템 모두 만족하면 while loop 탈출
            break

        for _ in list(W.keys()):    #####  1일 - 10일째에서 물건 만족하는지 일단 계산해봄
            temp_D = Counter(discount[left:right + 1]) 
            if W[_] == temp_D[_]:   ##### 만족하면 cnt += 1
                cnt += 1
            if (_ not in temp_D) or (W[_] < temp_D[_]):     ##### want 안의 물건이 없거나 부족해 -> 날짜를 하루씩 증가시켜서 2일 - 11일을 살펴봐 -> 찾을 때까지 반복해
                left += 1
                right += 1
    return left+1                   ##### 그때 몇 번째 날인지 return해 줘
    ###### left였는지 left+1이었는지 기억이 안남

#print(solution(A, B, C))
