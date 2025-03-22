from stats import count_words, count_chars, sort_list
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        file_contents: str = file.read()
    return file_contents

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath: str = sys.argv[1]
    text: str = get_book_text(filepath)
    word_count: str = count_words(text)
    sorted_list: dict = sort_list(count_chars(text))

    print(
        "============ BOOKBOT ============",
        f"\nAnalyzing book found at {filepath}...",
        "\n----------- Word Count ----------",
        f"\nFound {word_count} total words",
        "\n--------- Character Count -------",
        f"\n{str(sorted_list)
        .replace(", ", "\n")
        .replace("'", "")
        .replace("{", "")
        .replace("}", "")}"
    )

if __name__ == "__main__":
    main()