def alphabet_position(letter):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter in alpha:
        return alpha.index(letter)
    elif letter in alpha1:
        return alpha1.index(letter)
    else:
        return ord(letter)



#message = input("what is your message?")
#rotate = input("what is your rotation amt?")
def rotate_character(char, rot):

    rotated_index = (alphabet_position(char) + rot) % 26
    if char.isupper():
        return chr(rotated_index + ord("A"))
    if char.islower():
        return chr(rotated_index + ord("a"))
    else:
        return char
