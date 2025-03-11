def get_num_words ():
    with open('/home/theone/workspace/bookbot/books/frankenstein.txt') as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = 0
        for word in words:
            num_words += 1
        print(f"{num_words} words found in the document")
get_num_words()
