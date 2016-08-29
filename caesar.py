#from helpers import alphabet_position, rotate_character
#from sys import argv, exit
#print("I know that these are the words the user typed on the command line:", argv)



ALPHABET_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def alphabet_position(letter):
   alphabet = ALPHABET_LOWERCASE if letter.islower() else ALPHABET_UPPERCASE
   return alphabet.index(letter)

def rotate_char(char, rotation):
   if not char.isalpha():
       return char

   alphabet = ALPHABET_LOWERCASE if char.islower() else ALPHABET_UPPERCASE
   new_pos = (alphabet_position(char) + rotation) % 26
   return alphabet[new_pos]

def encrypt(text, rotation):
   answer = ""
   for char in text:
       answer += rotate_char(char, rotation)
   return answer
