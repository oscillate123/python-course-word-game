import file_handler as fh
import game_functions_2 as func_2


def random_word_picker(word_list):
    random_word = func_2.random_list_element(word_list=word_list)
    return random_word


class Compare:
    def __init__(self, guess, word):
        self.guess = guess
        self.word = word

    def compare_words(self):
        # compares the programs guess with the user chosen word and parse it
        # source: https://qph.fs.quoracdn.net/main-qimg-dbe0252936d6b28a6644faa17953f9ef

        if self.guess == self.word:
            return print(f"Grattis! Gissning: {self.guess} | Ord: {self.word}")
        else:
            for g_idx, g_char in enumerate(self.guess):
                for w_idx, w_char in enumerate(self.word):
                    if g_idx == w_idx and g_char == w_char:




if __name__ == "__main__":
    WORDS_FILE = "words.txt"
    word_list = fh.file_reader(read_file=WORDS_FILE, encoding='ISO-8859-1')  # returns list
    random_word = random_word_picker(word_list=word_list)

    x = Compare(guess=random_word, word="äckel")
    y = x.compare_words()
    print(y)