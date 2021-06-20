def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        sort_array = sorted(array[commands[i][0]-1: commands[i][1]])
        answer.append(sort_array[commands[i][2]-1])
    return answer
