def random_word_picker(word_list):
    pass


class Compare:
    def __init__(self, guess, word):
        self.guess = guess
        self.word = word

    def compare_words(self):
        # compares the user guess with the chosen word and displays which character is correct
        # source: https://qph.fs.quoracdn.net/main-qimg-dbe0252936d6b28a6644faa17953f9ef

        if self.guess != self.word:

            correct_letters_and_pos = ["" for _ in range(len(self.word))]
            correct_letters = []
            incorrect_letters = []

            for g_idx, g_char in enumerate(self.guess):
                print_counter = 0
                count = self.word.count(g_char)

                for w_idx, w_char in enumerate(self.word):
                    if g_char == w_char and g_idx == w_idx:
                        # if the characters and character indexes are matching.

                        correct_letters_and_pos[w_idx] = g_char
                        print(f"Bokstaven {g_char} är på rätt position.")
                        if count < 2:
                            break  # so we don't keep testing/checking, as long as there are no similar characters

                    elif g_char == w_char and g_idx != w_idx:
                        # if the characters are the same, but not in the same position.

                        if count == 1:
                            print(f"Bokstaven {g_char} finns i ordet, men på en annan position")
                            correct_letters.append(g_char)
                            break  # so we don't keep testing/checking
                        elif count != 1 and print_counter == 0:
                            print_counter += 1  # we increment with 1, so if the condition gets True again, it won't
                            # print the same message in the same inner-loop process.
                            print(f"Det finns flera {g_char} i ordet, men denna är inte på rätt position.")
                            correct_letters.append(g_char)

            if len(incorrect_letters) == 5:
                print("Ingen av bokstäverna angivna finns i ordet. Vänligen försök igen.")

            return False

        elif self.guess == self.word:
            print(f"Rätt gissning! Ordet var {self.word}")
            return True
