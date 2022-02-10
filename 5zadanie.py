from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
answer = []

def get_jokes(n, flag=False):
    for i in range(n):
        random_one = choice(nouns)
        random_two = choice(adverbs)
        random_three = choice(adjectives)
        otvet = f'{random_one} {random_two} {random_three}'
        answer_two = []
        print(otvet)
        if flag == True:
            answer_two = otvet.split()
            for nouns_answer in nouns:
                for i in answer_two:
                    if nouns_answer == i:
                        nouns.remove(nouns_answer)
        for answer_adverbs in adverbs:
                for i in answer_two:
                    if answer_adverbs == i:
                        adverbs.remove(answer_adverbs)


        for answer_adjectives in adjectives:
            for i in answer_two:
                if answer_adjectives == i:
                    adjectives.remove(answer_adjectives)
get_jokes(n=3, flag=True)
