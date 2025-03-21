def count_words(text: str) -> str:
    words: int = 0
    for word in text.split():
        words += 1
    return f"{words} words found in the document"