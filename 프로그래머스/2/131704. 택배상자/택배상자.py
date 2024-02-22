from collections import deque


def solution(order):
    order = deque(order)
    main_c = deque(sorted(order))
    sub_c = deque()
    t = []
    
    while main_c:
        if sub_c and order[0] == sub_c[-1]:
            sp = sub_c.pop()
            t.append(sp)
            order.popleft()
            
        mpl = main_c.popleft()
        if order[0] == mpl:
            t.append(mpl)
            order.popleft()
        else:
            sub_c.append(mpl)
    
    while sub_c and sub_c[-1] == order[0]:
        sp = sub_c.pop()
        opl = order.popleft()     
        t.append(sp)
            
    return len(t)