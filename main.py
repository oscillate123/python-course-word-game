import file_handler as fh
import game_functions as func
import game_explaination as game_exp

if __name__ == "__main__":

    words_file = "words.txt"
    game_exp.get_game_description(boolean=True)
    word_list = fh.file_reader(read_file=words_file, encoding='ISO-8859-1')  # returns list
    random_word = func.random_list_element(word_list=word_list)

    def main():
        while True:
            user_input = input("dasdasd")

            if user_input == "1":
                pass

            if user_input == "2":
                user_guess = func.guess_input()
                run = func.Compare(guess=user_guess, word=random_word)
                run_done = run.compare_words()

                if run_done:
                    return

    main()
