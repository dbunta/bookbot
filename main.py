def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        char_counts = get_letter_counts(file_contents)
        print_report(word_count, char_counts)

    
def get_letter_counts(file_contents):
    char_counts = {}
    for c in file_contents.lower():
        if c in char_counts:
            char_counts[c] += 1
        elif c.isalpha():
            char_counts[c] = 0
    return char_counts

def print_report(word_count, char_counts):
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print()
        for k, v in char_counts.items():
            print(f"The \'{k}\' character was found {v} times")



main()