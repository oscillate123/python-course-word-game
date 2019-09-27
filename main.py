import file_handler as fh
import game_functions_1 as func_1
import game_functions_2 as f

if __name__ == "__main__":
    counter_1 = 0
    counter_2 = 0
    WORDS_FILE = "words.txt"
    word_list = fh.file_reader(read_file=WORDS_FILE, encoding='ISO-8859-1')  # returns list
    random_word = f.random_list_element(word_list=word_list)

    leader_or_player = f.console_init()

    # if leader_or_player == "leader":
    """
    hämta lista och ta fram ett random ord (variabel word_list och funktion leader_input)
    ta bort ordet ur listan, om det inte är rätt, för att spara tid och möda senare
    leader_input har en return, [värde1, värde2]
    loopa genom varje ord i word_list
        x = Compare(kanel, baner, leader)
        för varje ord, kolla om resultatet av Compare.game_words_selector [värde1, värde2]
        har samma resultat som leader_input [värde1, värde2]
        
        leader_input = [3, 0]
        x.game_mode_selector (= [3, 0])
        
        om x.game_mode_selector (= [3, 0]) == leader_input
            gör inget - för då kan det vara rätt ord
        om x.game_mode_selector (= [3, 0]) != leader_input
            ta bort ordet från listan, så vi filtrerar bort orden som det inte kan vara
            
            
    hämta lista och ta fram ett random ord (variabel word_list och funktion leader_input)
    etc.
    """

    if leader_or_player == "leader":
        the_words_list = word_list.copy()

        flag = True

        while flag:










        # the_newlist = []
        #
        # if len(the_newlist) == 0:
        #     the_random_word = f.random_list_element(word_list=the_words_list)
        # else:
        #     the_random_word = f.random_list_element(word_list=the_newlist)
        #
        # hints = f.leader_input(random_word=the_random_word)
        #
        # for word in the_words_list:
        #     run = f.ParseGuess(guess=word, word=the_random_word)
        #     result = run.words_analyzer()[1]
        #
        #     print(f"hints {hints}")
        #     print(f"result {result}")
        #
        #     if hints == result:
        #         the_newlist.append(word)
        #     else:
        #         pass
        #
        # print(the_newlist)

    while leader_or_player == "player":
        counter_2 += 1
        user_guess = f.player_input(the_answer=random_word)
        run = f.ParseGuess(guess=user_guess, word=random_word)
        run_done = run.run_game()

        if run_done:
            if counter_2 == 1:
                print(f"Du gissade bara {counter_2} gång!")
            else:
                print(f"Du gissade {counter_2} gånger.")
            break
