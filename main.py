def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    words = word_counter(text)
    character_dict = character_count(text)
    characters_sorted_list = sort_characters(character_dict)

    # print(f"The text of to book located at {
    #       path_to_file} is below: \n \n \n {text}")
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{words} found in this book.")

    # print(f"The count of all characters can be seen below \n {character_dict}")

    for item in characters_sorted_list:
        if not item["character"].isalpha():
            continue
        print(f"The '{item['character']}' character was found {
              item['number']} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_counter(text):
    words = text.split()
    return len(words)


def character_count(text):
    charcater_dict = {}
    for i in text:
        lowercase = i.lower()
        if lowercase in charcater_dict:
            charcater_dict[lowercase] += 1
        else:
            charcater_dict[lowercase] = 1
    return charcater_dict


def sort_dict(dic):
    return dic["number"]


def sort_characters(character_dict):
    sorted_list = []
    for character in character_dict:
        sorted_list.append(
            {"character": character, "number": character_dict[character]})
    sorted_list.sort(reverse=True, key=sort_dict)

    return sorted_list


main()


# print("hello world")
#
#
# def main():
#     with open("./books/frankenstein.txt") as f:
#         file_contents = f.read()
#         print(file_contents)
#
#
# # main()
#
#
# def word_count():
#     with open("./books/frankenstein.txt") as f:
#         file_contents = f.read()
#         words = file_contents.split()
#         print(f"{len(words)} words found in the document")
#         return len(words)
#
#
# word_count()
#
#
# character_count = {}
#
#
# def word_counter():
#     with open("./books/frankenstein.txt") as f:
#         file_contents = f.read()
#         for letter in file_contents.lower():
#             if letter in character_count:
#                 character_count[letter] += 1
#             else:
#                 character_count[letter] = 1
#
#         # print(character_count)
#
#
# word_counter()
#
# value_list = []
#
#
# def report():
#     for k in character_count:
#         if k.isalpha():
#             print(f"The '{k}' charaster was found {character_count[k]} times")
#
#
# report()
