import json
import csv
import nltk
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer('german')

# print(stemmer.stem('chiens'))


def find_highest(data):
    # for item in data.keys():
    highest_volume = max(data.values())
    for keyword, volume in data.items():
        if volume == highest_volume:
            return f'{keyword}|{volume}'


words_map = dict()

with open('data.csv') as start_file:
    reader = csv.reader(start_file, delimiter='|')
    next(reader)

    for line in reader:
        phrase, volume = line
        phrase = phrase.strip().split()
        root_form = [stemmer.stem(word) for word in phrase]
        str_root_form = ' '.join(sorted(root_form))
        if str_root_form in words_map:
            words_map[str_root_form].update({line[0].strip(): int(volume)})
        else:
            words_map[str_root_form] = {line[0].strip(): int(volume)}

# print(json.dumps(words_map, indent=4))

for item in words_map:
    print(find_highest(words_map[item]))
