
english_russian_translator = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(eng_word):
    if eng_word[0] == eng_word[0].upper():
        eng_word = eng_word.lower()
        return english_russian_translator[eng_word].capitalize()
    else:
        return english_russian_translator[eng_word]


print(num_translate_adv('two'))
print(num_translate_adv('Two'))