import wordscore
import sys
import copy
from collections import Counter

# Implement a buy/spend system. 
# Word from sowpods needs to "buy" letters from the "player_rack". 
# A wildcard will allow word from sowpods to buy the space with any letter it has
# If Word can affor it, it gets to be a valid word and gets sent for score processings
# After the word/score dictionary is built, print it 

args = sys.argv

def main() : 
    
    sowpods = openfile("sowpods.txt")
    valid_words = []

    #First, count up the quantity of each letter in the "player_rack"
    player_rack = dict(Counter(list(args[1].upper())))
    
    for word in sowpods: 
        #Append the valid word to valid_words list if checkvalid returns true
        if checkvalid(word, player_rack):
            valid_words.append(word)
     
    #Merge the score list with thier respective valid_word
    result = list(map(lambda x, y:(x,y), wordscore.score_word(valid_words), valid_words))
    
    #Print the results
    for a, b in sorted(result, reverse=True): 
        print(a, b)
    
        
def checkvalid(word, player_rack):
    """This function processes which letters "word" can buy from the player_rack
       In order for it to be a valid word, it must be able to buy all of it's letters
       In essence this is a comparator of dictionarys. 
    """    
    total_wildcards = countwildcards(player_rack)
    used_letters = []
    word = dict(Counter(list(word.upper())))
    
    #keep track of used keys()
    
    #Sum of wildcard values is less than or equal to unused_letters
    #total_wildcards <= sum(used_letters.values())
    
    for count, letter in enumerate(word):
        #check if letter is in the player rack at all, if is it must also be affordable by word   
        if letter in player_rack.keys() and word[letter] <= player_rack[letter]:
            used_letters.append(letter)  #append to our used letters

            if count == len(word)-1 :
                #unused_letters = copy.deepcopy(word)
                #del unused_letters[used_letters]
                print(sum(word.values()), total_wildcards, len(used_letters))
                return True

        else:
            return False

def countwildcards(player_rack):
    
    total_wildcards = 0
    wildcard = ["?", "*"]

    for letter in player_rack:
        if letter in wildcard:
            total_wildcards += player_rack[letter]
            
    return total_wildcards 

def openfile(filename):
    """returns a list of filename contents"""    
    file_content = []
    
    with open(filename, 'r+') as file:
        for row in file:
            file_content.append(row.rstrip())
    
    return file_content

if __name__ == "__main__":
    main()
