from collections import Counter


def solution(X, Y):
    answer = 0
    x_cnt, y_cnt = {}, {}
    x = list(map(int, X))
    y = list(map(int, Y))
    common = {}
    nums = []

    if len(x) > len(y):
        x, y = y, x

    x_cnt = Counter(x)
    y_cnt = Counter(y)

    for i in range(10):
        if x_cnt[i] > 0 and y_cnt[i] > 0:
            common[i] = min(x_cnt[i], y_cnt[i])

    if len(common) == 0:
        return "-1"
    else:
        for i in list(common.keys()):
            for j in range(common[i]):
                nums.append(str(i))

    nums = sorted(nums, reverse=True)
    nums = ''.join(nums)
    return nums


#print(solution("100", "123450"))
