def main():
   
    total_words = 0
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    

    letter_counts = {}
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            char = char.lower()  # Convert to lowercase
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    
    words = text.split()
    
    for word in words:
        total_words = total_words + 1
    print(f"--- Begin report of {book_path} ---")
    print(f"{total_words} words found in the document")
    for letter in sorted(letter_counts, key=letter_counts.get, reverse=True):
        
        print(f"The letter '{letter}' appears {letter_counts[letter]} times.")
    return words
    


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()