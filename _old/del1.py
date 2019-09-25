import file_handler as rf

words_db = rf.file_reader("words.txt", encoding="ISO-8859-1")
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


""" t_tt_ """

""" for word in check_word_list """
#       if word == check_result
#            append.word
#

