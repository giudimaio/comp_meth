"""First assignment.
"""

import argparse
import logging
import time
import string

#...Setting the basic level...
logging.basicConfig(level=logging.DEBUG)

#Define a function which needs the file path (or simply file name if it is in the same dir):
def process(file_path):

    start_time = time.time()
    
	#Display it's correctly reading the file:
    logging.info("Reading input file %s...", file_path)

	'''
	#Try to open the file from line 8526 but failed..
    if args.sk:
    	with open(file_path) as input_file:
    		for line in range(8526):
    			text = input_file.readline(line)
    			print(text)
    			line += 1
    else:
    	with open(file_path) as input_file:					
    		text = input_file.read()
    '''
    
    #Correct version to open file:
    with open(file_path) as input_file:					
    text = input_file.read()
    
    num_chars = len(text)
    logging.info("Done, %d characters found.", num_chars)

	#Create a dict.
    #The syntax for dict is {key:value} with key variable in this case (ch represents the character in ascii string). 
    #string.ascii gives a string 'abcdefgh...', while '0' stands for the value I want to associate to the keys 'a', 'b',... So I am initializing 0 for all keys

    char_dict = {ch: 0 for ch in string.ascii_lowercase}

	#Go inside the input file:
    for ch in text:
    	#.lower() converts all uppercases to lowercases, for example 'A' ---> 'a':
        ch = ch.lower()
        #Implements the counter for obtaining frequencies. If the ch-key appears in dict --> 
        # ---> increments the VALUE related to CH-KEY:
        if ch in char_dict:
           		char_dict[ch] += 1
            
        #Another way to do it (not so obvious..):
        # try:
        #     char_dict[ch.lower()] += 1
        # except KeyError:
        #     pass

	#The following gives the elapsed time from start (start_time) to now (time.time):
    elapsed_time = time.time() - start_time
    logging.info("Done in %.3f seconds.", elapsed_time)
    
    #Sum the letters (VALUES IN DICT) to find the total number of letters (not characters!):
    num_letters = sum(char_dict.values())
    #Go inside the dict {ch:num} and divide the num (frequency for 'a', for example) by total number, for having the percent:
    for ch, num in char_dict.items():
    	#.....I dont understand the purpose of f inside print.....
        print(f"{ch} -> {num / num_letters:.3%}")


#"if" is for doing everything in the __main__:
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=str, help="Path to the input file")
    parser.add_argument('--sk', action='store_true',help='Skip preamble')
    args = parser.parse_args()

    process(args.infile)

    
    
    
    
    
    
    
