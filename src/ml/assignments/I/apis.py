from collections import Counter
from math import log2


def calculate_entropy(input):
    counts = Counter(input)
    ans = 0
    original_size = len(input)
    for k, v in counts.items():
        P = v/original_size
        ans -= P*log2(P)
    return ans


def calculate_information_gain(original, splitted):
    original_size = len(original)

    splitted_entropy = 0
    for s in splitted:
        splitted_entropy += calculate_entropy(s)*len(s)/original_size

    original_entropy = calculate_entropy(original)

    ans = original_entropy-splitted_entropy
    return ans


def calculate_gain_ratio(original, splitted):
    information_gain = calculate_information_gain(original, splitted)

    # This splitted entropy is different from the one of Calculate Information Gain API.
    original_size = len(original)
    splitted_entropy = 0
    for s in splitted:
        P = len(s)/original_size
        splitted_entropy -= P*log2(P)

    ans = information_gain/splitted_entropy
    return ans