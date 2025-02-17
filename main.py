def main():

    book_name = "frankenstein"
    book_location = "books/" + book_name + ".txt"
    with open(book_location) as f:
        file_contents = f.read()
        #print(file_contents)
        print("Beginning Report for " + book_name)
        print("Total word count: " + str(count_words(file_contents)))
        print("")
        print("")

        char_dict = count_characters(file_contents)
       # for kvp in char_dict:
       #      print(f"{kvp}: {char_dict[kvp]}")

        alpha_dict = trim_non_alpha(char_dict)
        alpha_dict = sort_dict_count(alpha_dict)
        print_dict(book_name, alpha_dict)

def count_words(string):
        word_count = string.split()
        return len(word_count)

def count_characters(string):
    letter_dict = {}
    string = string.lower()
    for letter in string:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def trim_non_alpha(dictionary):
    alpha_dict = {}
    for kvp in dictionary:
        if kvp.isalpha():
            alpha_dict[kvp] = dictionary[kvp]
    return alpha_dict

def sort_dict_count(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

def print_dict(title, dictionary):
    print("Character count for " + title)
    print("")
    for kvp in dictionary:
        print(f"'{kvp}' was counted {dictionary[kvp]} times.")
    print("")
    print("Finished reporting character count for " + title)

main()