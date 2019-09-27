import file_handler as fh
import game_functions_2 as func_2


def random_word_picker(word_list):
    random_word = func_2.random_list_element(word_list=word_list)
    return random_word


# if __name__ == "__main__":
#     WORDS_FILE = "words.txt"
#     word_list = fh.file_reader(read_file=WORDS_FILE, encoding='ISO-8859-1')  # returns list
#     random_word = func_2.random_list_element(word_list=word_list)
#     y = False
#
#     while not y:
#
#         x = Compare(guess=random_word, word="äckel")
#         y = x.compare_words()[-1]