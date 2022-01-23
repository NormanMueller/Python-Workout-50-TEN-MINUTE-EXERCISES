from collections  import Counter
words = ['this', 'is', 'an', 'elementary', 'test', 'example', 'edfeeeee']
def most_repeated_letters(word_list):
    return sorted(word_list, key = lambda a: Counter(a).most_common(1)[0][1])

most_repeated_letters(words)

