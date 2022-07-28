from collections import Counter
# 소문자 counter 안 됨. Counter로 입력받은 숫자에 0 - 9까지가 몇 개 인지를 센다.

def solution(X, Y):
    answer = 0
    x_cnt, y_cnt = {}, {}
    x = list(map(int, X)) # 자리수별로 분해
    y = list(map(int, Y))
    common = {} # 공통부분을 담을 공간
    nums = [] # 공통 숫자들을 차례대로 append할 공간

    # 길이가 긴 것을 y에 무조건 보낸다
    if len(x) > len(y):
        x, y = y, x
    
    # 숫자를 세 줘
    x_cnt = Counter(x)
    y_cnt = Counter(y)
    
    # 0 - 9까지를 보면서 공통 숫자가 있다면 두 개중에 더 작은 것을 common dict에 추가해 줘
    for i in range(10):
        if x_cnt[i] > 0 and y_cnt[i] > 0:
            common[i] = min(x_cnt[i], y_cnt[i])

    # 공통 숫자가 없으면 common의 원소가 없음 > -1을 return해라
    if len(common) == 0:
        return "-1"
    # 공통 숫자가 있는 개수대로 nums에 string 타입으로 추가한다
    else:
        for i in list(common.keys()):
            for j in range(common[i]):
                nums.append(str(i))

    # 내림차순 정렬 후, 그 숫자를 다 합쳐줘라
    nums = sorted(nums, reverse=True)
    nums = ''.join(nums)
    return nums


#print(solution("100", "123450"))
