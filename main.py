import file_handler as fh
import game_functions as f
import ParseUserGuess as PUG

if __name__ == "__main__":

    WORDS_FILE = "words.txt"
    file_content = fh.file_reader(read_file=WORDS_FILE, encoding='ISO-8859-1')  # returns list
    # random_word = f.random_list_element(word_list=file_content)
    random_word = "oscar"

    leader_or_player = f.console_init()

    if leader_or_player == "leader":
        counter_1 = 0
        word_list = file_content.copy()
        flag = True

        while flag:
            r_word = f.random_list_element(word_list)
            new_list = f.find_related_words(word_list=word_list, robot_guess=r_word, hints=f.leader_input(r_word))
            word_list = new_list
            new_list.remove(r_word)

            if len(new_list) == 0:
                print(f"Programmet ger upp.")
                flag = False

    elif leader_or_player == "player":
        counter_2 = 0
        flag = True

        while flag:
            counter_2 += 1
            user_guess = f.player_input(the_answer=random_word)
            run = PUG.ParseGuess(guess=user_guess, word=random_word)
            run_done = run.run_game()

            if run_done:
                if counter_2 == 1:
                    print(f"Du gissade bara {counter_2} gång!")
                    flag = False
                else:
                    print(f"Du gissade {counter_2} gånger.")
                    flag = False
