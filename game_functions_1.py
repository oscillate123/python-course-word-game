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

            correct_letters_and_pos = ["" for _ in range(len(self.word))]
            correct_letters = []
            word = self.word
            word_letters = list(word)

            for w_idx, j in enumerate(self.word):
                for g_idx, i in enumerate(self.guess):
                    if i == j and g_idx == w_idx:
                        correct_letters_and_pos[w_idx] = i

                        print(f"Bokstaven {i} är på rätt position.")

                    if i == j and g_idx != w_idx:
                        correct_letters.append(i)

                        print(f"Bokstaven {i} finns i ordet.")

            # return [correct_letters_and_pos, correct_letters, word_letters]
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