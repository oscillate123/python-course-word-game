import file_handler as fh
import funktioner as func

words_file = "words.txt"

if __name__ == "__main__":
    x = fh.file_reader(read_file=words_file, encoding='ISO-8859-1')  # returns list
    y = func.random_word(x)
    print(y)
