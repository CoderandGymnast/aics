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
