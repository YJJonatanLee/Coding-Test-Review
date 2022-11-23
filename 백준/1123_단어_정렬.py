N = int(input())

word_list = []
for _ in range(N):
    word_list.append(str(input()))
    
word_list_n = list(set(word_list))

answer_list = sorted(word_list_n, key = lambda x: (len(x), x))

for answer in answer_list:
    print(answer)
