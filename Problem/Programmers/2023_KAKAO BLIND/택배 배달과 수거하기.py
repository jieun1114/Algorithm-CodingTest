def solution(cap, n, deliveries, pickups):
    answer = 0

    while deliveries or pickups:

        del_cap = cap
        pick_cap = cap

        while deliveries and deliveries[-1] == 0:
            deliveries.pop()
        while pickups and pickups[-1] == 0:
            pickups.pop()

        answer += max(len(deliveries), len(pickups)) * 2

        while deliveries and del_cap > 0:
            del_cnt = deliveries.pop()
            if del_cap < del_cnt:
                deliveries.append(del_cnt - del_cap)
                del_cap = 0
            else:
                del_cap -= del_cnt

        while pickups and pick_cap > 0:
            pick_cnt = pickups.pop()
            if pick_cap < pick_cnt:
                pickups.append(pick_cnt - pick_cap)
                pick_cap = 0
            else:
                pick_cap -= pick_cnt

    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
print(solution(4, 4, [25, 24, 51, 0], [51, 0, 0, 49]))