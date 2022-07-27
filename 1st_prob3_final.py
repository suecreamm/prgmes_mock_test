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
            q.popleft()
            result += 1
            sub_searching(q, sub, max_q)
        else:
            sub.append(i)
    return result


def sub_searching(queue, sub_li, N):
    global result
    while sub_li and queue:
        if queue[0] != sub_li[-1]:
            break
        else:
            sub_li.pop()
            queue.popleft()
            result += 1 
