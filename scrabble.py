import wordscore
import sys


def open_file(filename):
# open file, create list of words
    sowpods = []
    with open('sowpods.txt', 'r+') as f:
        for row in f:
            sowpods.append(row.rstrip())








# define main function
def main():
	# find valid words from sowpods
	valid_words = []
	for word in sowpods:
		counter = 0
		list_letters = list(args[1].upper())
		
        #This is the word match algorithm
        for character in word:
			for letter in list_letters:
				if character == letter:
					counter += 1
					list_letters.pop(list_letters.index(letter))
					if counter == len(word) and len(word) <= len(args[1]):
						valid_words.append(word)
						break



	# print results
	result = zip(score_list, valid_words)

	def getKey(item):
		return item[0]
	result = sorted(result, key = getKey, reverse = True)

	for item in result:
		print '%i, %s' % item



# take a command line argument
args = sys.argv
if len(sys.argv) < 2:
	print('Usage: scrabble.py [RACK]')
else:
	main()
