def count_words(text: str) -> str:
    words: int = 0
    for word in text.split():
        words += 1
    return f"{words} words found in the document"

def count_chars(text: str) -> dict:
    char_count: dict = {}
    for word in text.split():
        for char in word:
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count