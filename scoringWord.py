import re
import math


def score_word(word, usage_freq, position_freq):
    # Score word using the provided dictionary usage_freq where the letter is
    # worth the number of points corresponding to its frequency, plus a bonus
    # based on how common that letter is in that position in the word,
    # but each additional time that letter is used in the word, its points are
    # reduced.

    seen = {}
    word_score = 0

    for position in range(0, 5):
        letter = word[position]
        letter_score = (usage_freq[letter] +
                        (position_freq[position][letter] * 3))

        if letter in seen:
            reduction_factor = seen[letter] * 4
            letter_score = math.floor(letter_score / reduction_factor)
            seen[letter] = seen[letter] + 1
        else:
            seen[letter] = 1

        word_score = word_score + letter_score
    return word_score


def get_five_letter_words(wordlist):
    eligible_words = []
    for word in wordlist:
        if len(word) != 5:
            continue

        if re.match('[^a-zA-Z]', word):
            # In case the provided wordlist contains any non-letter characters
            continue

        eligible_words.append(word.lower())
    print(str(len(eligible_words)) + ' five-letter words')
    return eligible_words


def get_position_frequency(wordlist):
    # for each letter position, 0-4, determine how often the letter is
    # in that position
    position_count = {}
    for position in range(0, 5):
        position_count[position] = {}
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            position_count[position][letter] = 0

    for word in wordlist:
        for position in range(0, 5):
            letter = word[position]
            position_count[position][letter] = (
                    position_count[position][letter] + 1)

    return position_count


def get_usage_frequency(wordlist):
    frequency_count = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        frequency_count[letter] = 0

    for word in wordlist:
        for letter in word:
            frequency_count[letter] = frequency_count[letter] + 1
    return frequency_count


def get_best(data):
    eligible_words = get_five_letter_words(data)
    usage_frequency = get_usage_frequency(eligible_words)
    position_frequency = get_position_frequency(eligible_words)

    word_scores = {}
    for word in eligible_words:
        word_scores[word] = score_word(
            word, usage_frequency, position_frequency)

    scored_rank = sorted(word_scores, key=word_scores.get, reverse=True)
    return scored_rank[0]
