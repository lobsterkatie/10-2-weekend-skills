# To work on the advanced problems, set to True
ADVANCED = False

from string import punctuation
from collections import Counter

def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'do': 1, 'porcupine': 2, 'see': 1}

    """

    # NOTE: I *did* in fact want this to be case-insensitive, and punctuation-
    # insensitive, so I changed the test output of the third test to reflect
    # that.

    word_counts = {}

    # Clean the input string by removing punctuation and lowercasing everything
    input_string = input_string.translate(None, punctuation).lower()

    # Get the words in the input string as a list
    word_list = input_string.split()

    # For each word in the input text, see if it's already in word_counts
    # Increment its counter if it is, add it and set the count to 1 if not
    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def find_common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in at least one list and is present
    in both lists, return it each time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """

    # NOTE: not to be difficult, but the output you're describing doesn't make
    # sense, IMHO... If one list has two copies of something and the second list
    # has three copies, what they have in common is two copies, not three. I
    # mean... right??

    common_elements = []

    # get a count of all the elements of each list
    element_counts1 = Counter(list1)
    element_counts2 = Counter(list2)

    for element in element_counts1:
        # if element (from first list) is also in second list
        if element_counts2[element] != 0:
            # then add that element the list of in-common elements
            # here is where I think the output doesn't make sense
            # changing 'max' to 'min,' however, would make it make sense
            num_copies = max(element_counts1[element],
                             element_counts2[element])
            for i in range(num_copies):
                common_elements.append(element)

    return common_elements


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """

    common_elements = []

    # get a count of all the elements of each list
    element_counts1 = Counter(list1)
    element_counts2 = Counter(list2)

    for element in element_counts1:
        # if element (from first list) is also in second list
        if element_counts2[element] != 0:
            # then add that element the list of in-common elements
            common_elements.append(element)

    return common_elements


def get_sum_zero_pairs(input_list):
    """Given a list of numbers, return list of x,y number pair lists where x + y == 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """

    zero_sum_pairs = []

    for num in input_list:
        # if num's additive inverse is in the list
        if (num * -1) in input_list:
            # then add the pair to our list (sorted so neg one is always first,
            # which will help with de-duping in the next step)
            zero_sum_pairs.append(sorted([num, num * -1]))

    # remove duplicates and then turn it back into a list (zsp = zero-sum pair)
    unique_zsps = set(tuple(pair) for pair in zero_sum_pairs)
    zero_sum_pairs = list(unique_zsps)

    return zero_sum_pairs


def remove_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    Do this without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    # is this cheating?
    # if so, I could use code (the for loop) from count_unique above
    word_counts = Counter(words)

    return word_counts.keys()


def encode(phrase):
    """Given a phrase, return the encoded string.

    Replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u".

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """

    # Hmmm... this also kinda feels like cheating...
    # So, without writing the whole thing out, one could do it manually thus:
    #   - iterate an index i through range(:len(phrase))
    #   - have four if's checking phrase[i] against e, a, t, and i, respectively
    #   - under each if, replace that character with the new one and continue
    phrase = phrase.replace("e", "p")
    phrase = phrase.replace("a", "d")
    phrase = phrase.replace("t", "o")
    phrase = phrase.replace("i", "u")

    # it should also be noted that if you wanted to do a full replacement
    # encoding (every letter gets replaced by a new one), you couldn't do it
    # sequentially like this (a new 'a,' for instance, would look the same as
    # an old 'a,' and would therefore get written over if the replace-the-a's
    # pass came after the replace-with-an-a pass). You'd have to replace each
    # letter with a non-letter (digit, punctuation mark, etc) first and then
    # replace each of those with the correct new letter

    return phrase


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """

    word_length_dict = {}

    for word in words:
        length = len(word)
        # if there are already words of that length in the dictionary
        if word_length_dict.get(length) is not None:
            # then add current word to the list of words of that length
            word_length_dict[length].append(word)
        # otherwise, add it as a new dictionary entry
        else:
            word_length_dict[length] = [word]

    return list(word_length_dict.iteritems())


def get_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> get_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> get_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    eng_to_pirate_dict = {"sir": "matey",
                          "hotel": "fleabag inn",
                          "student": "swabbie",
                          "boy": "matey",
                          "madam": "proud beauty",
                          "professor": "foul blaggart",
                          "restaurant": "galley",
                          "your": "yer",
                          "excuse": "arr",
                          "students": "swabbies",
                          "are": "be",
                          "lawyer": "foul blaggart",
                          "the": "th'",
                          "restroom": "head",
                          "my": "me",
                          "hello": "avast",
                          "is": "be",
                          "man": "matey"}

    # turn the string into a list of words
    phrase_as_list = phrase.split()

    # go through each word in turn, replacing it with its pirate translation,
    # if applicable
    for i, word in enumerate(phrase_as_list):
        if word in eng_to_pirate_dict:
            phrase_as_list[i] = eng_to_pirate_dict[word]

    # turn the list back into a string
    pirate_version = " ".join(phrase_as_list)

    return pirate_version

# End of skills. See below for advanced problems.
# To work on them, set ADVANCED=True at the top of this file.
############################################################################


def adv_get_top_letter(input_string):
    """Given an input string, return a list of letter(s) which appear(s) the most the input string.

    If there is a tie, the order of the letters in the returned
    list should be alphabetical.

    For example:
        >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:
        >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Spaces do not count as letters.

    """

    return ''


def adv_alpha_sort_by_word_length(words):
    """Given a list of words, return a list of tuples, ordered by word-length.

    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.
    Now try doing it with only one call to .sort() or sorted(). What does the
    optional "key" argument for .sort() and sorted() do?

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    return []


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
