import wordscore
import sys
from collections import Counter

def main():
    
    valid_words = []
    
    sowpods = open_file("sowpods.txt")
	
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
                    
	# print results
    result = zip(wordscore.score_word(valid_words), valid_words)

    def getKey(item):
        print("Inside Get_Key")
        print(item[0])
        return item[0]
   
    result = sorted(result, key = getKey, reverse = True)

    for item in result:
        print('%i, %s' % item)


def open_file(filename):
    """returns a list of filename contents"""    
    file_content = []
    
    with open(filename, 'r+') as file:
        for row in file:
            file_content.append(row.rstrip())
    
    return file_content



# take a command line argument
args = sys.argv

if len(sys.argv) < 2:
	print('Usage: scrabble.py [RACK]')
else:
	main()
