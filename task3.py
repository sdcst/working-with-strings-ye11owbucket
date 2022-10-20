#!python3
'''
##### Task 3
Split a string into 2 halves and insert a line break in the middle.  If doing so cuts a word in half, add a dash to the first line.  You will need to make use of the

len(str) function
this function returns the length of the string

(2 points)
'''

from abc import get_cache_token


def split(input):
    count = len(input)
    count = count / 2
    if count %2 != 0:
        count = round(count,1)
    count =int(count) 
    if input[count] == " " or input[count-1] == " ":
        fstring = input[:count] + "\n" + input[count:]
    else:
        fstring = input[:count] + "-\n" + input[count:]
    return fstring

if __name__ == "__main__":
    sentence = "There is a big balloon in the blue sky"
    assert split(sentence) == "There is a big ball-\noon in the blue sky"

    sentence = "I am a fat cat"
    assert split(sentence) == "I am a \nfat cat"

    sentence = "I was a fat cat"
    assert split(sentence) == "I was a\n fat cat"
