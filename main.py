import file_handler as fh
import game_functions as gf
import input_functions as input
# import parse_user_guess as pug

if __name__ == "__main__":

    file_content = fh.file_reader(read_file="words.txt", encoding='ISO-8859-1')  # returns list
    leader_or_player = input.console_input()

    if leader_or_player == "leader":
        gf.leader(words_list=file_content)

    elif leader_or_player == "player":
        gf.player(words_list=file_content)
