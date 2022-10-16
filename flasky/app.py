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
        regexes.append(bannedWord)
        for i in range(0, len(bannedWord)):
            regex = list(bannedWord)
            regex[i] = '[^a-z]'
            regexes.append("".join(regex)+"$")
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
def check_input_num(text, regex):
    text_word_list = parse_input(text)
    # censored = ""

    banned_count = 0

    for textIndex in text_word_list:
        if re.match(regex, textIndex):
            banned_count += 1
            # censored += ("*" * len(textIndex))
            # if we want we can print the offending text
            # print(textIndex)
    #     else:
    #         censored += textIndex
    #     censored += " "
    # return censored
    return (banned_count * 100) / len(text_word_list)

def check_input_censored(text, regex):
    text_word_list = parse_input(text)
    censored = ""

    banned_count = 0

    for textIndex in text_word_list:
        is_match = re.match(regex, textIndex)
        if is_match:
            # partially censor words
            # censored += textIndex[:is_match.span()[0]]
            banned_count += 1
            censored += ("*" * len(textIndex))

            # censored += ("*" * (is_match.span()[1] - is_match.span()[0]))
            # censored += textIndex[is_match.span()[1]:]
        else:
            censored += textIndex
        censored += " "
    return censored
    # return (banned_count * 100) / len(text_word_list)


#@app.route('/')
@app.route('/info', methods=['GET', 'POST'])
def run():
    args = request.args
    dict_args = args.to_dict()

    if 'userText' not in args.to_dict():
        return "ERROR"

    print(f'{dict_args["userText"]}')
    print('testing')
    banned_list = read_banned_file('banned.txt')
    # banned_list = read_banned_file('banned_clean.txt')
    banned_regex = generate_regex(banned_list)

    text = f'{dict_args["userText"]}'
    # text = file.readline()
    # text.strip("\n")
    print(text)
    print(check_input_num(text, banned_regex))
    # return "".join(str(check_input_num(text, banned_regex)))
    return "".join(str(check_input_censored(text.lower(), banned_regex)))


if __name__ == '__main__':
    app.run(debug=True)
