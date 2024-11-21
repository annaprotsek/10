import os


def create_input_file():
    text = """Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: \
once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \
'and what is the use of a book,' thought Alice 'without pictures or conversation?'"""

    with open("input.txt", "w", encoding="utf-8") as file:
        file.write(text)
    print("Файл input.txt створено з текстом книги.")

def process_text():

    with open("input.txt", "r", encoding="utf-8") as file:
        text = file.read()

    words = text.lower().replace(",", "").replace(".", "").replace("'", "").replace(":", "").split()
    unique_words = sorted(set(words)) 

    print(f"Кількість унікальних слів: {len(unique_words)}")

    with open("output.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(unique_words))
    print("Файл output.txt створено. Унікальні слова записано.")

def main():

    create_input_file()

    process_text()

if __name__ == "__main__":
    main()
