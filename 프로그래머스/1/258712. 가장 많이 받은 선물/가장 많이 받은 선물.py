from collections import defaultdict


def solution(friends, gifts):
    # 선물을 주고받은 기록
    history = {
        friend: {"gift": defaultdict(int), "received": defaultdict(int)}
        for friend in friends
    }
    rank = {friend: 0 for friend in friends}

    set_friends = set(friends)

    # 선물 지수
    def history_index(friend):
        x = sum(history[friend]["gift"].values())
        y = sum(history[friend]["received"].values())
        return x - y

    # 선물을 주고받지 않은 사람
    def history_difference(friend):
        y = set(
            list(history[friend]["gift"]) + list(history[friend]["received"]) + [friend]
        )
        return set_friends - y

    # 선물 기록 갱신
    for gift in gifts:
        giver, recipient = gift.split()
        history[giver]["gift"][recipient] += 1
        history[recipient]["received"][giver] += 1

    # 받은 선물 계산
    for friend in friends:
        pivot_index = history_index(friend)
        pivot_difference = history_difference(friend)

        # 선물을 주고받은 기록이 하나도 없을때 처리
        if pivot_difference:
            for name in pivot_difference:
                if pivot_index > history_index(name):
                    rank[friend] += 1

        # 선물을 주고받은 기록이 있을때 처리
        for giver, give_cnt in history[friend]["gift"].items():
            if giver in history[friend]["received"]:
                received_cnt = history[friend]["received"][giver]
                if give_cnt > received_cnt or (
                    give_cnt == received_cnt and pivot_index > history_index(giver)
                ):
                    rank[friend] += 1
            else:
                rank[friend] += 1

    # 가장 많이 선물받은 값 반환
    answer = max(rank.values())
    return answer
