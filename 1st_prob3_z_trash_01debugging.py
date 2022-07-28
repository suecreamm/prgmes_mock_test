from collections import deque

result = 0


def solution(order):
    sub = [0]                   ##### stack 구조로
    global result
    q = deque(order)
    max_q = max(q)

    for i in list(range(1, max_q+1)):
        if len(q) == 0:
            break
        if i == q[0]:

            previous_item = q.popleft()
            result += 1

            if sub_searching(q, sub, max_q) == 0:
                continue
                # break 했을때는 안됐음
            else:
                sub_searching(q, sub, max_q)
        else:
            sub.append(i)
    return result


def sub_searching(queue, sub_li, N):
    global result
    if result >= N:
        pass
    if len(sub_li) == 1 or len(queue) == 0:
        return N
    if queue[0] == sub_li[-1]:
        sub_li.pop()
        queue.popleft()
        result += 1
        sub_searching(queue, sub_li, N)
    else:
        return 0
    return N


print(solution([1, 2, 3, 4, 5]))
