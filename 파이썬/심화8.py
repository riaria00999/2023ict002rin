N = int(input())
group_words = 0

for _ in range(N):
    word = input()
    is_group_word = True
    
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            continue
        elif word[i] in word[i+1:]:
            is_group_word = False
            break
    
    if is_group_word:
        group_words += 1

print(group_words)
