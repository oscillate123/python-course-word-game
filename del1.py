import read_file as rf

words_db = rf.get_words()
words_list = words_db.copy()
hints_list = ["a", "t", "r"]
matches = []


def checker():

    for word in words_list:
        hits = ["_" for _ in word]
        for idx, char in enumerate(word):
            for hint in hints_list:
                if char == hint:
                    hits[idx] = char
                    break

        if len(hints_list) <= sum(hits):
            matches.append(word)
        elif len(hints_list) >= sum(hits):
            words_list.remove(word)

checker()


""" a_tr_ """

""" for word in check_word_list """
#       if word == check_result
#            append.word
#            

