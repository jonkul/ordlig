"""
Functions for ordlig helper
"""


filename = "ordlig5.csv"
new_filename = ''
g = []
y = []
gn = ["", "", "", "", ""]


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
    with open(file()) as filehandle:
        content = filehandle.read()
    return content


def read_lines():
    """
    Opens the text file, ordlig5 by default
    """
    with open(file()) as filehandle:
        line_content = filehandle.readlines()
    return line_content


def grey():
    """
    Add greyed out letters to global g.
    """
    global g

    print("Current greyed out letters: " + str(g))
    new = input("Add another one (e.g 'y' or 'm'): ")
    g.append(new)

    return g


def yellow():
    """
    Add yellow letters to global y.
    """
    global y

    print("Current yellow letters: " + str(y))
    new = input("Add another one (e.g '0y' or '4m'): ")
    y.append(new)

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

    return gn


def ten():
    """
    Run filters and print words
    """
    global g, y, gn
    
    line_content = read_lines()
    if g:
        line_content = filterg(line_content)
    if y:
        line_content = filtery(line_content)
    if gn:
        line_content = filtergn(line_content)
    
    print("\n" + str(len(line_content)) + " filtered words:")
    for line in line_content[0:30]:
        print("       " + line[0:5])
    
    return ""


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
        for x in range(len(y)):
            if not str(y[x][1]) in line:
                add_line = False
        for x in range(len(y)):
            if str(y[x][1]) == str(line[x]):
                add_line = False
        if add_line == True:
            filtered.append(line)
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
        for x in range(len(y)):
            if gn[x] != '':
                if gn[x] != line[x]:
                    add_line = False
        if add_line == True:
            filtered.append(line)
    return filtered
