from collections import defaultdict

def solution(id_list, report, k):
    #신고한 사람:[신고당한사람들 리스트]
    de_dict = defaultdict(list)
    #신고당한 사람:[신고한사람 리스트]
    ac_dict = defaultdict(list)
    #정지당한 사람 리스트
    sus_list = []
    #신고메일 리스트
    answer_list = len(id_list) * [0]
    
    for i in report:
        de_person = i.split(" ")[0]
        ac_person = i.split(" ")[1]
        ac_dict[ac_person].append(de_person)
        de_dict[de_person].append(ac_person)
    
    #신고한 사람:[신고당한 사람들 리스트]에서 신고당한 사람들 겹치는 것 제거
    for de in de_dict:
        de_dict[de] = list(set(de_dict[de]))
    
    #정지당한 사람 리스트 만들기
    for ac in ac_dict:
        ac_dict[ac] = len(set(ac_dict[ac]))
        if ac_dict[ac] >= k:
            sus_list.append(ac)
    
    #de_dict에 있는 id를 돌며 신고당한 사람들 리스트와 정지당한 리스트가 얼마나 겹치는지 확인
    for id in de_dict:
        for i in de_dict[id]:
            for j in sus_list:
                if i == j:
                    answer_list[id_list.index(id)] += 1

    return answer_list
