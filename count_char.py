def count_characters(text):
    char_count = {}
    text_lower = text.lower()
    
    for char in text_lower:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    
    return char_count

def main():
    path_to_file = "books/frankenstein.txt"
    
    with open(path_to_file) as f:
        file_contents = f.read()
        char_count = count_characters(file_contents)
        print("Character counts in the book:")
        for char, count in char_count.items():
            print(f"{char}: {count}")

if __name__ == "__main__":
    main()