import file_handler as fh
import game_functions_1 as func_1
import game_functions_2 as func_2
import game_explaination as game_exp

if __name__ == "__main__":

    words_file = "words.txt"
    game_exp.get_game_description(boolean=False)
    word_list = fh.file_reader(read_file=words_file, encoding='ISO-8859-1')  # returns list
    random_word = func_2.random_list_element(word_list=word_list)

    def main():

        counter_1 = 0
        counter_2 = 0

        while True:
            user_input = input("\nVill du vara ledare eller spelare?\n 1 - ledare | 2 - spelare\n >> ")

            if user_input == "1":
                func_1.random_word_picker(word_list=word_list)

            if user_input == "2":
                counter_2 += 1
                user_guess = func_2.guess_input()
                run = func_2.Compare(guess=user_guess, word=random_word)
                run_done = run.compare_words()

                if run_done:
                    print(f"Du gissade {counter_2} gånger.")
                    return

    main()
