# this program takes a user input and gives the decrypted word or sentence

import os.path

def main():
    decrypted_msg = getInputFile()
    print("The decrypted message is:")
    print(decrypted_msg)



def getInputFile():
    """The purpose of this function is to take the user input.
    If the file exists then it will return the decrypt function"""
    user_file = input('Enter the input filename: ')
    if os.path.exists(user_file):
        return decrypt(user_file)
    while not os.path.exists(user_file):
        user_file = input('Invalid filename extension. Please re-enter the input filename: ')
        if os.path.exists(user_file):
            return decrypt(user_file)


def decrypt(user_file):
    """The purpose of the function is to decrypt the given file inputted by user_file.
    We get user_file from the getInputFile function"""
    with open(user_file, 'r') as view:
        content = view.readlines()
        view.close()
        key = int(content[0])
        sentence = content[1].lower().rstrip()
        decrypted_text = []
        final_string = ""
        for letter_index in range(len(sentence)):
            letter = sentence[letter_index]
            if ' ' == letter:
                decrypted_text.append(ord(letter))
            else:
                to_number = ord(letter)
                for individual_key in range(key):
                    to_number -= 1
                    if to_number < ord('a'):
                        to_number = ord('z')
                decrypted_text.append(to_number)


        for i in range(len(decrypted_text)):
            to_letter = chr(decrypted_text[i])
            final_string += to_letter

        return final_string



if __name__ == '__main__':
    main()






