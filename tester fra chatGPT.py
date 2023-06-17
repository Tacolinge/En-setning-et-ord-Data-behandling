import re


regex_expressions = [
    r'^-',
    r'\d',
    r'^.$',
    r'-'
]


def check_regex_match(word, regex_expressions):
    for exp in regex_expressions:
        if not re.search(exp, word):
            continue
        else: return False #print("false en match som betyr ordet kan IKKE brukes")
    return True #print("True ingen re match ordet kan brukes")

test_ord = ["-as", "A", "a", "vise", "1", "1q","q5","q 5", "o-r-d-vise", "qwe1234056789", "A-dur", "dure", "moll"]


for ord in test_ord:
    if check_regex_match(ord, regex_expressions):
        print(ord, "= True kan brukes")
    #else: print(ord, "= Flase kan IKKE brukes")

