from stats import count_words

def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        file_contents: str = file.read()
    return file_contents

def main() -> None:
    print(count_words(get_book_text("books/frankenstein.txt")))

if __name__ == "__main__":
    main()