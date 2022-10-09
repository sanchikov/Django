from django import template
import re

register = template.Library()

WORDS_TO_CATCH = [
    'stupid',
    'Post2',
    'title',
    'Automobile',
    'about',
    'post1',
    'comment',
    'is',
    'one',
    'stupid',
    'свинья',
    'негр',
]


# Регистрируем наш фильтр под именем censor, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()  # -> {{ text|censor }}
def censor(text_to_check):

    new_text = re.sub(r'[^\w\s]', '', text_to_check)
    word_list = new_text.strip().split()

    new_stop_list = [x.lower() for x in WORDS_TO_CATCH]

    for word in word_list:
        word_len = len(word)
        if (word.lower() in new_stop_list) or (
                (word.lower()[-1] == 's') and (word.lower()[:word_len - 1] in new_stop_list)):
            substitute = word[0] + '*' * (len(word) - 2) + word[-1]  # about -> a***t
            text_to_check = text_to_check.replace(word, substitute)

    return text_to_check