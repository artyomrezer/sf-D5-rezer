from django import template
 
register = template.Library()

@register.filter(name='censor')
def censor(string):
    if isinstance(string, str):
        bad_words_list = ['bad_word1', 'bad_word2', 'bad_word3']
        #либо загрузить список плохих слов из внешнего файла.

        for bad_word in bad_words_list:
            if bad_word in string:
                string = string.replace(bad_word, '***')
    else:
        raise ValueError('Подана не строка, обработка не возможна')
        
    return string