import sys
from wordscore import score_word
from collections import Counter


"""Get arguments from command line,
    check to see if len(args) is in expected range
    otherwise print usage and exit""" 
args = sys.argv

if len(args) > 2:
    print("Usage: python scrabble.py <rack> ")
    sys.exit(1)

def run_scrabble() : 
    """Begins running the scrabble program"""
    
    # Load the sowpods text file, initialize a valid words list
    sowpods = open_file("sowpods.txt")
    valid_words = []

    # Creat a dictionary with the occurence of letter in the player_rack
    player_rack = dict(Counter(list(args[1].upper())))
    
    # Begin itteration through sowpods, checking if they are valid words
    for word in sowpods: 
        if check_valid(word, player_rack):
            # Append valid words found to valid_words list
            valid_words.append(word)
     
    # Merge the score list with thier respective valid_word
    result = list(map(lambda x, y:(x,y), 
             score_word(valid_words), 
             valid_words))
    
    # Sort result from highest to lowest before return
    return (sorted(result, reverse = True, 
            key=lambda x: x[0]),
            len(valid_words))
        
def check_valid(word, player_rack):
    """Implements a transactional test,
       For each word in sowpods, it must be able to "buy" letters from the player_rack.
       A wildcard allows sowpods words to buy any unmatched letter from the player_rack.  
    """    

    # Count the occurences of wildcards in the player rack
    # Create a dictionary of the letter occurences in the word.
    total_wildcards = count_wilds(player_rack)
    word = dict(Counter(list(word.upper())))
    
    # Begin itteration through the word
    for count, letter in enumerate(word):
        #  If letter is in the player rack at all, if is it must also be affordable by word   
        if (letter in player_rack.keys() and 
                word[letter] <= player_rack[letter]):
            #  See if we've reached the end of word and have run out of wildcards
            if (count == len(word)-1 and 
                    total_wildcards <= 0):
                return True

        # If letter is not in the player rack at all, 
        # see if there's a wildcard available to buy it with
        elif word[letter] <= total_wildcards:
            total_wildcards -= word[letter]
            if total_wildcards < 0: 
                return False
            elif count == len(word) - 1:
                return True

        #Catch all conition
        else:
            return False

def count_wilds(player_rack):
    """Counts the number of wild cards in the player rack
       Returns an integer"""

    #Initialize total_wildcards and define wildcard characters   
    total_wildcards = 0
    wildcard = ["?", "*"]

    # Iterate through letters in player_rack and add to total_wildcards
    # when a match is found
    for letter in player_rack:
        if letter in wildcard:
            total_wildcards += player_rack[letter]
            
    return total_wildcards 

def open_file(filename):
    """returns a list of filename contents"""    
    file_content = []
    
    with open(filename, 'r+') as file:
        for row in file:
            file_content.append(row.rstrip())
    
    return file_content

if __name__ == "__main__":
    print(run_scrabble())
