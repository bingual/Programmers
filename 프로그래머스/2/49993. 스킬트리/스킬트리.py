def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        order = []
        
        for char in skill_tree:
            if char in skill:
                order.append(char)
        
        if all(order[i] == skill[i]  for i in range(len(order))):
            answer += 1
    
    return answer