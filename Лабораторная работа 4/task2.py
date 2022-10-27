def get_count_char(str_):

    str_dict = {}
    DEFAULT_COUNT = 0

    str_ = "".join(str_.split())
    str_ = str_.lower()

    for s in str_:
        if s.isalpha():
          str_dict[s] = str_dict.get(s, DEFAULT_COUNT) + 1

    return str_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

def get_percent_char(str_dict):

    percent_dict = {}
    total_count = sum(str_dict.values())

    for s, count in str_dict.items():
        percent = round(count / total_count * 100, 2)
        percent_dict[s] = percent_dict.get(s, percent)

    return percent_dict

print(get_count_char(main_str))
print(get_percent_char(get_count_char(main_str)))
