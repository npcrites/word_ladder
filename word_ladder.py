#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony',
    'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots',
    'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    f = open(dictionary_file, "r")
    dict_words = []
    for word in f:
        dict_words.append(word.strip())
    if start_word == end_word:
        return [start_word]
    if end_word not in dict_words:
        return None
    stack = []
    stack.append(start_word)
    queue = []
    queue.append(stack)
    while len(queue) != 0:
        x = queue[0]
        queue = queue[1:]
        top_word = x[-1]
        for wd in list(dict_words):
            if _adjacent(wd, top_word):
                if wd == end_word:
                    x.append(wd)
                    return x
                else:
                    new_stack = x[:]
                    new_stack.append(wd)
                    queue.append(new_stack)
                    dict_words.remove(wd)


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if ladder == []:
        return False
    for (i, entry) in enumerate(ladder):
        if i <= len(ladder) - 2 and _adjacent(ladder[i], ladder[i + 1]) is False:
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    diff = 0
    if (len(word1) != len(word2)):
        return False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff += 1
    if diff == 1:
        return True

    else:
        return False
