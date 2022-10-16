from flask import Flask, request, render_template, flash, redirect
import re

app = Flask(__name__)


def read_banned_file(filename):
    # Get list from file
    banned_list = []
    file = open(filename, 'r')
    for word in file:
        bare_word = word.strip("\n")
        banned_list.append(bare_word)
    # for index in bannedList:
    #     print(index)
    return banned_list


def generate_regex(banned_list):
    regexes = []
    for bannedWord in banned_list:
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
def parse_input(text):
    return text.split()


# text is a string, bannedRegex is the list of all possible regexes
# returns integer that represents count of words from bannedRegex
def check_input(text, regex):
    text_word_list = parse_input(text)

    banned_count = 0

    for textIndex in text_word_list:
        if re.match(regex, textIndex):
            banned_count += 1
            # if we want we can print the offending text
            # print(textIndex)
    return (banned_count * 100) / len(text_word_list)


@app.route('/', methods=['GET', 'POST'])
def run():
    banned_list = read_banned_file('banned.txt')
    banned_regex = generate_regex(banned_list)

    file = open("input.txt", 'r')
    text = file.readline()
    text.strip("\n")
    print(text)
    print(check_input(text, banned_regex))
    return "".join(str(check_input(text, banned_regex)))


if __name__ == '__main__':
    app.run()
