import read_file as rf

words_db = rf.get_words()
words_list = words_db.copy()
hints_list = []
matches = []


def test():
    print("Vilka 3 bokstäver får ordet innehålla?")

    while len(hints_list) < 3:
        hints_list.append(input(f"Bokstav {len(hints_list) + 1}:"))

        for word in words_list:
            hits = [0 for _ in word]
            for idx, char in enumerate(word):
                for hint in hints_list:
                    if char == hint:
                        hits[idx] = 1

            if len(hints_list) <= sum(hits):
                matches.append(word)
            elif len(hints_list) >= sum(hits):
                words_list.remove(word)

