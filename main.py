import re


def readBannedFile(filename):
    # Get list from file
    bannedList = []
    file = open(filename, 'r')

    for word in file:
        bare_word = word.strip("\n")
        bannedList.append(bare_word)

    # for index in bannedList:
    #     print(index)
    return bannedList


def generateRegex(bannedList):
    regexes = []
    temp = "/"
    for bannedWord in bannedList:
        if len(bannedWord) <= 2:
            continue

        for i in range(0, len(bannedWord)):
            regex = list(bannedWord)
            regex[i] = '.?'
            regexes.append("".join(regex))
            # temp.join('(?:% s)' % '|'.join(regex))
            # print(temp)
    temp = '(?:% s)' % '|'.join(regexes)
    # print(temp)
    return temp

# should return a list of strings, given a space-separated string input.
def parseInput(text):
    return text.split()


# text is a string, bannedRegex is the list of all possible regexes
# returns integer that represents count of words from bannedRegex
def checkInput(text, regex):
    textWordList = parseInput(text)

    bannedCount = 0

    for textIndex in textWordList:
        if re.match(regex, textIndex):
            bannedCount += 1
            # if we want we can print the offending text
            # print(textIndex)

    return bannedCount


bannedList = readBannedFile('banned.txt')
bannedregex = generateRegex(bannedList)

file = open("input.txt", 'r')
text = file.readline()
text.strip("\n")
print(text)

print(checkInput(text, bannedregex))
