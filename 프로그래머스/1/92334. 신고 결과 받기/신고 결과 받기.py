from collections import defaultdict


def solution(id_list, report, k):
    # 신고/정지 명단
    users = {id: {"target": set(), "banned_cnt": 0} for id in id_list}
    report_cnt = defaultdict(int)  # 신고당한 횟수

    # 신고 처리
    for item in report:
        reporter, target = item.split()
        # 명단에 피신고자가 없을 경우 추가하고 신고당한 횟수 카운트
        if target not in users[reporter]["target"]:
            users[reporter]["target"].add(target)
            report_cnt[target] += 1

    # 처리 결과 메일통보
    for user, cnt in report_cnt.items():
        if cnt >= k:
            # 정지 처리한 피신고자인 만큼 카운트
            for reporter, target in users.items():
                if user in target["target"]:
                    users[reporter]["banned_cnt"] += 1

    # 각 유저가 처리 결과 메일을 받은 횟수 반환
    answer = [user["banned_cnt"] for user in users.values()]
    return answer