"""
Functions for ordlig helper
"""

import string
from operator import itemgetter

validchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖabcdefghijklmnopqrstuvwxyzåäöéê"
filename = "ordlig5b.csv"
new_filename = ''
g = []
y = []
gn = ["", "", "", "", ""]
values = {}
words = {}


def file():
    """
    Check if new filename selected. Returns old or new filename.
    """
    if new_filename == '':
        return filename
    return new_filename


def read_file():
    """
    Opens the text file, ordlig5 by default
    """
    with open(file(), 'r', encoding='utf-8') as filehandle:
        content = filehandle.read()
    return content


def read_lines():
    """
    Opens the text file, ordlig5 by default
    """
    with open(file(), 'r', encoding='utf-8') as filehandle:
        line_content = filehandle.readlines()
    return line_content


def clear():
    """
    Opens the text file, ordlig5b by default
    """
    global g
    global y
    global gn

    g = []
    y = []
    gn = ["", "", "", "", ""]

    return ""


def grey():
    """
    Add greyed out letters to global g.
    """
    global g

    print("Current greyed out letters: " + str(g))
    new = input("Add another one (e.g 'y' or 'asdf'): ")
    for x in new:
        if not x in g:
            g.append(x)

    print("\nAdded grey letter:")
    print(str(g))

    return g


def yellow():
    """
    Add yellow letters to global y.
    """
    global y

    print("Current yellow letters: " + str(y))
    new = input("Add another one (e.g '0y' or '4m'): ")
    if not new in y:
        y.append(new)

    print("\nAdded yellow letter:")
    print(str(y))

    return y


def green():
    """
    Add green letters to global gn.
    """
    global gn

    print("Current green letters: " + str(gn))
    new = input("Add another one (e.g '0y' or '4m'): ")
    pos = int(new[0])
    gn[pos] = new[1]

    print("\nAdded green letter:")
    print(str(gn))

    return gn


def greyrm():
    """
    Remove last added entry in global g.
    """
    global g

    g.remove(g[-1])

    print("\nRemoved last added grey letter, list now contains:")
    print(str(g))

    return g


def yellowrm():
    """
    Remove last added entry in global y.
    """
    global y

    y.remove(y[-1])

    print("\nRemoved last added yellow letter, list now contains:")
    print(str(y))

    return y


def greenrm():
    """
    Remove last added entry in global gn.
    """
    global gn

    gn.remove(gn[-1])

    print("\nRemoved last added green letter, list now contains:")
    print(str(gn))

    return gn


def letter_frequency():
    """
    Counts the frequency of letters.
    """
    global values

    string_content = read_file().lower()

    char_list = []
    for i in string_content:
        if i in validchars:
            char_list += i

    dic = {}
    for char in char_list:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1

    dic_list = dic.items()
    dic_sorted = sorted(dic_list, key=itemgetter(1), reverse=True)
    dic_cut = dic_sorted[0:]
    dic_2 = {key: value for key, value in dic_cut}

    # perc = count_letters()

    for key, value in dic_2.items():
        values[key] = str(value) # + " | " + str(round(value*100/perc, 1)) + "%"

    #for key, value in values.items():
    #    print(key + ":", value)
    return values

    # print(values["a"])


def word_score(word):
    """
    Scores a word, based on how popular its letters are
    """
    global values, words
    fword = []
    score = 0

    if not values:
        letter_frequency()

    # remove duplicate letters
    for letter in word:
        if not letter in fword:
            fword.append(letter)
    # print(str(fword))

    for letter in fword:
        score += int(values[letter])
    # print(str(score))
    
    return score


def filterg(line_content):
    """
    Filters out words with greyed out letters
    """
    global g
    filtered = []
    for line in line_content:
        add_line = True
        for x in g:
            if x in line:
                add_line = False
        if add_line == True:
            filtered.append(line)
    return filtered


def filtery(line_content):
    """
    Filters out words that don't contain yellow letters, 
    or words with the yellow letter in that position
    """
    global y
    filtered = []
    for line in line_content:
        add_line = True
        line2 = line[:5]
        for x in range(len(y)):
            if not str(y[x][1]) in line:
                add_line = False
        for x in range(len(y)):
            s = y[x][1] #a
            i = int(y[x][0]) #2
            if str(s) == str(line2[i]):
                add_line = False
        if add_line == True:
            filtered.append(line2)
    return filtered


def filtergn(line_content):
    """
    Filters out words that don't contain the green letters
    in that position
    """
    global gn
    filtered = []
    for line in line_content:
        add_line = True
        for x in range(len(gn)):
            if gn[x] != '':
                if gn[x] != line[x]:
                    add_line = False
        if add_line == True:
            filtered.append(line)
    return filtered


def output():
    """
    Run filters and print words
    """
    global g, y, gn
    
    # read dictionary
    line_content = read_lines()
    words = {}
    
    # apply filters if necessary
    if gn:
        line_content = filtergn(line_content)
    if y:
        line_content = filtery(line_content)
    if g:
        line_content = filterg(line_content)

    # add word and its word_score to dictionary words
    for line in line_content:
        words[line[:5]] = word_score(line[:5])

    # sort the dictionary
    dic_list = words.items()
    dic_sorted = sorted(dic_list, key=itemgetter(1), reverse=True)
    dic_cut = dic_sorted[0:31]
    dic_2 = {key: value for key, value in dic_cut}

    # print output
    print("\n" + str(len(line_content)) + " filtered words:")
    for key, value in dic_2.items():
        print(key + ":", value)

    #for line in line_content[0:30]:
    #    print("       " + line[0:5])
    
    return ""
