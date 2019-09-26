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
        # compares the user guess with the chosen word and displays which character is correct
        # source: https://qph.fs.quoracdn.net/main-qimg-dbe0252936d6b28a6644faa17953f9ef

        if self.guess == self.word:
            print(f"Programmet gissade rätt:\n{self.guess} = {self.word}")
            return True

        elif self.guess != self.word:

            for g_idx, g_char in enumerate(self.guess):

                for w_idx, w_char in enumerate(self.word):
                    if g_char == w_char and g_idx == w_idx:
                        # if the characters and character indexes are matching.

                        print(f"Bokstaven {g_char} är på rätt position.")
                        break  # we stop testing/checking, to save time

                    elif g_char in self.word and g_idx == w_idx:
                        print(f"Bokstaven {g_char} är rätt men på fel plats.")
                        break

            return False

        else:
            raise RuntimeError("Something is wrong here!")


if __name__ == "__main__":
    WORDS_FILE = "words.txt"
    word_list = fh.file_reader(read_file=WORDS_FILE, encoding='ISO-8859-1')  # returns list
    random_word = random_word_picker(word_list=word_list)

    x = Compare(guess=random_word, word="äckel")
    y = x.compare_words()
    print(y)