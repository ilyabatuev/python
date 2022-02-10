dict_translate = {
    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
}

def num_translate(say_number):
    key = dict_translate.get(say_number)
    if key:
        return dict_translate.get(say_number)
    else:
        print(None)



















