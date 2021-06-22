def solution(citations):
    answer = 0
    sort_citations = sorted(citations)
    for i in range(len(sort_citations)):
        arr_h = []
        arr_h = sort_citations[i:].copy()
        if len(arr_h) >= sort_citations[i]:
            answer = sort_citations[i]
    return answer
