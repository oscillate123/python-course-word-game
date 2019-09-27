import file_handler as fh
import game_functions_2 as func_2


def random_word_picker(word_list):
    func_2.random_list_element(word_list=word_list)
    return random_word


class Compare:
    def __init__(self, guess, word):
        self.guess = guess
        self.word = word

    def compare_words(self):
        # compares the program guess with the chosen word and parse it
        # source: https://qph.fs.quoracdn.net/main-qimg-dbe0252936d6b28a6644faa17953f9ef

        if self.guess == self.word:
            print(f"Programmet gissade rätt:\n{self.guess} = {self.word}")
            return True

        elif self.guess != self.word:

            correct_letters_and_pos = ["" for _ in range(len(self.word))]
            correct_letters = []
            incorrect_letters = []
            word = self.word
            word_letters = list(word)

            for w_idx, j in enumerate(self.word):
                for g_idx, i in enumerate(self.guess):
                    if i == j and g_idx == w_idx:
                        correct_letters_and_pos[w_idx] = i

                        print(f"Bokstaven {i} är på rätt position.")

                    elif i == j and g_idx != w_idx:
                        correct_letters.append(i)

                        print(f"Bokstaven {i} finns i ordet.")

                    elif i != j and g_idx != w_idx and i not in correct_letters and i not in correct_letters_and_pos:
                        incorrect_letters.append(i)
                        print(f"Bokstaven {i} finns inte i ordet.")

            return [correct_letters_and_pos, correct_letters, word_letters, False]

        else:
            raise RuntimeError("Something is wrong here!")


if __name__ == "__main__":
    WORDS_FILE = "words.txt"
    word_list = fh.file_reader(read_file=WORDS_FILE, encoding='ISO-8859-1')  # returns list
    random_word = func_2.random_list_element(word_list=word_list)
    y = False

    while not y:

        x = Compare(guess=random_word, word="äckel")
        y = x.compare_words()[-1]