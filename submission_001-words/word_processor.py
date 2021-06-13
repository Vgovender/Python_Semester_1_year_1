
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    
    return([x.lower() for x in (split(',.;? ', text)) if len(x) > 0])


def words_longer_than(length, text):
    return([x for x in convert_to_word_list(text) if len(x) > length])

def words_lengths_map(text):
    text = convert_to_word_list(text)
    var = sorted(list(map(lambda x: len(x),text)))
    dictionary = {}
    for i in var:
        dictionary[i] = var.count(i)
    return dictionary

def letters_count_map(text):
    text = ''.join(convert_to_word_list(text))
    var = sorted(list(map(lambda x: x,text)))
    dictionary = {}
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in alpha:
        dictionary[i] = var.count(i)
    return dictionary


def most_used_character(text):
    if text == '':
        return None
    else:
        text = letters_count_map(text)
        a = sorted(text.items(), key=lambda x: x[1], reverse=True)
        return (a[0][0])

# def most_used_character(text):
#     count = 0
#     alpha = ''
#     # print(text)
#     var = sorted(list(map(lambda x: x,text)))
#     dict = {}
#     list2 = var[:]
#     for i in range(len(text)):
#         dict[i] = var.count(i)
#         # print(var.count(i))
#         if var.count(i) >= count and i > 0:
#             count = var.count(i)
#             alpha = var[i]
#     return alpha
#     # print(var[30:31])


if __name__ == '__main__':
    text_input = 'These are indeed interesting, an obvious understatement, times. What say you?'
    print(convert_to_word_list(text_input))
    print(words_longer_than(10, text_input))
    print(words_lengths_map(text_input))
    print(letters_count_map(text_input))
    print(most_used_character(text_input))