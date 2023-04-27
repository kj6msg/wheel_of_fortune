#!/usr/bin/env python3

# Wheel of Fortune Bonus Round Letters
# Copyright (c) 2023 Ryan Clarke, licensed under the MIT License.

import collections
import csv
import matplotlib.pyplot as plt
import re
import sys

def main() -> int:
    with open('bonus_round.csv', newline='') as f:
        reader = csv.DictReader(f)

        letter_counts = collections.Counter()
        for line in reader:
            if line['WHEN USED'] == 'BR':
                # strip non-alphabetic characters
                alpha_only = re.sub('[^A-Za-z]+', '', line['PUZZLE'])
                letter_counts += collections.Counter(alpha_only)

    letters, frequency = zip(*letter_counts.most_common())

    colors = []
    for l in letters:
        if l in 'RSTLNE':
            colors.append('red')
        else:
            colors.append('blue')

    plt.bar(letters, frequency, color=colors)
    plt.title('Wheel of Fortune Bonus Round Letters Histogram')
    plt.xlabel('Letter')
    plt.ylabel('Frequency')
    plt.show()

    return 0

if __name__ == '__main__':
    sys.exit(main())
