
def score_word(valid_words): 
    """This scores words according to the score function provided"""

    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}

    score_list = []

    for word in valid_words:
        score = 0
        counter = 0

        for character in word:
            for letter, value in scores.items():
                if letter.upper() == character:
                    score = score + value
                    counter += 1

                if counter == len(word):
                    score_list.append(score)
                    break
        
        return score_list

#This can be done using a list comprehension