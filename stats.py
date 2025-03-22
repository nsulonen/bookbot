def count_words(text: str) -> str:
    words: int = 0
    for word in text.split():
        words += 1
    return words

def count_chars(text: str) -> dict:
    char_count: dict = {}
    for word in text.split():
        for char in word:
            char = char.lower()
            if char in char_count and char.isalpha():
                char_count[char] += 1
            elif char.isalpha():
                char_count[char] = 1
            else:
                pass
    return char_count

def sort_list(char_count: dict) -> dict:
    sorted_list: dict = {key: value for key, value in sorted(char_count.items(), key=lambda item: item[1], reverse=True)}
    return sorted_list
