import file_handler as fh
import game_functions as gf
import input_functions as input
# import parse_user_guess as pug

if __name__ == "__main__":

    file_content = fh.file_reader(read_file="words.txt", encoding='ISO-8859-1')  # returns list
    leader_or_player = input.console_input()

    if leader_or_player == "leader":
        # counter_1 = 0
        # word_list = file_content.copy()
        # flag = True
        #
        # while flag:
        #     r_word = gf.random_list_element(word_list)
        #  new_list = gf.find_related_words(word_list=word_list, robot_guess=r_word, hints=input.leader_input(r_word))
        #     word_list = new_list
        #     new_list.remove(r_word)
        #
        #     if len(new_list) == 0:
        #         print(f"Programmet ger upp.")
        #         flag = False
        gf.leader(words_list=file_content)

    elif leader_or_player == "player":
        # counter_2 = 0
        # flag = True
        # random_word = gf.random_list_element(word_list=words_list)
        #
        # while flag:
        #     counter_2 += 1
        #     user_guess = input.player_input(the_answer=random_word)
        #     run = pug.ParseGuess(guess=user_guess, word=random_word)
        #     run_done = run.run_game()
        #
        #     if run_done:
        #         if counter_2 == 1:
        #             print(f"Du gissade bara {counter_2} gång!")
        #             flag = False
        #         else:
        #             print(f"Du gissade {counter_2} gånger.")
        #             flag = False
        gf.player(words_list=file_content)
