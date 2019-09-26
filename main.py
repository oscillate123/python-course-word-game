import file_handler as fh
import game_functions_1 as func_1
import game_functions_2 as func_2

if __name__ == "__main__":
    counter_1 = 0
    counter_2 = 0
    WORDS_FILE = "words.txt"
    word_list = fh.file_reader(read_file=WORDS_FILE, encoding='ISO-8859-1')  # returns list
    random_word = func_2.random_list_element(word_list=word_list)

    user_input = func_2.console_master()

    if user_input == "1":
        func_1.random_word_picker(word_list=word_list)

    while user_input == "spelare":
        counter_2 += 1
        user_guess = func_2.guess_input(the_answer=random_word)
        run = func_2.Compare(guess=user_guess, word="t_tt_")
        run_done = run.compare_words()

        if run_done:
            if counter_2 == 1:
                print(f"Du gissade bara {counter_2} gång!")
            else:
                print(f"Du gissade {counter_2} gånger.")
            break
