import random


def read_data(path):
    try:
        words = []
        with open(path, 'r') as f:
            for line in f:
                words.append(line.strip().upper())
    except:
        return None
    else:
        return words

def normalize(word): # Replace the accents and special characters
    replacements = [
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ñ", "n"),
        ('"', "")
    ]
    for a, b in replacements:
        word = word.replace(a, b).replace(a.upper(), b.upper())
    return word

def get_word(words):
    try:
        limit = int(len(words)-1)
        random_word = random.randint(0, limit)
        word = words[random_word]
        word = normalize(word)
    except:
        return None
    else:
        return word