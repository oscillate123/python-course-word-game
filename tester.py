words_list = ["test", "hustak", "hus", "hund", "propp"]
hints_list = ["t", "h", "u"]
matches = []


for word in words_list:
    for hint in hints_list:
        if hint in word:
            matches.append(word)
        elif hint not in word and word in matches:
            matches.remove(word)

print(set(matches))
