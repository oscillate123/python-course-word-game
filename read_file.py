def get_words(read_file):
    with open(f"{read_file}", "r", encoding='ISO-8859-1') as file:
        reader = file.readlines()
        data = list(reader)
        data = [word.replace("\n", "") for word in data]
        return data
