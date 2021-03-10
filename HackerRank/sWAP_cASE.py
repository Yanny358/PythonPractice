def swap_case(s):
    words_list = []
    string = ''
    for letter in s:
        if letter == letter.lower():
            words_list.append(letter.upper())
            string = ''.join(words_list)
        elif letter == letter.upper():
            words_list.append(letter.lower())
            string = ''.join(words_list)
    return string


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# and of course there is swapcase() method which i didn't know exists
