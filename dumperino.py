from collections import Counter
from multiprocessing import Semaphore
from pdb import Restart

import sys
args = sys.argv

with open('sowpods.txt') as fin:
    lines = (word.strip().upper() for word in fin)
    words = [(word, Counter(word)) for word in lines]

rack = Counter('ZAEFIEE')

for scrabble_word, letter_count in words:
    # Using length here to limit output for example purposes
    if len(scrabble_word) >= 6 and not (letter_count - rack):
        print(scrabble_word)
        

# Implement a buy/spend system. 
# Word from sowpods needs to "buy" letters from the "player_rack". 
# A wildcard will allow word from sowpods to buy the space with any letter it has
# If Word can affor it, it gets to be a valid word and gets sent for score processings
# After the word/score dictionary is built, print it 

#First, count up the quantity of each letter in the "player_rack"
player_rack = Counter(list(args[1].upper()))

#Get the next word from sowpods






# find valid words from sowpods
    for word in sowpods:
        counter = 0
        player_rack = list(args[1].upper())
		
        #This is the word match algorithm
        for character in word:
            
            for rack_letter in player_rack:
                if character == rack_letter:
                    counter += 1
                    
                    player_rack.pop(player_rack.index(rack_letter))
                    
                    if counter == len(word) and len(word) <= len(args[1]):
                        valid_words.append(word)
                        break

