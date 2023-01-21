import math

ALPHABET = "\n !\"'(),-.0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def decrypt(text, key):
    decrypted = ""
    key = key.upper()
    text = text.upper()
    for position in range(len(text)):
        text_character = ALPHABET.index(text[position])
        key_character = ALPHABET.index(key[position % len(key)])
        decrypted_char = (text_character - key_character) % len(ALPHABET)
        decrypted += ALPHABET[decrypted_char]
    return decrypted


def get_frequencies(text):
    total = len(text)
    string = text.upper()
    letter_dict = {}

    for char in string:
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1

    # need to add a for loop to iterate through the dictionary and then divide each value by the total
    for key, value in letter_dict.items():
        letter_dict[key] = (value / total)

    return letter_dict


def cross_entropy(freqs1, freqs2):
    dict1 = freqs1
    dict2 = freqs2
    letter_list = []


    # iterate through the first dictionary and append the keys to the list
    for freq_letters1 in dict1.keys():
        letter_list.append(freq_letters1)

    # iterate through the first dictionary and append the keys to the list.
    for freq_letters2 in dict2.keys():
        # if statement is included that would not add if the letters already appeared in the same list
        if freq_letters2 not in letter_list:
            letter_list.append(freq_letters2)

    # this block is meant to check the minimum frequency of the first list
    freq_list1 = []
    for freq_numbers1 in dict1.values():
        if freq_numbers1 > 0:
            freq_list1.append(freq_numbers1)
            minimum_freq1 = min(freq_list1)

    # this block is meant to check the minimum frequency of the second list
    freq_list2 = []
    for freq_numbers2 in dict2.values():
        if freq_numbers2 > 0:
            freq_list2.append(freq_numbers2)
            minimum_freq2 = min(freq_list2)

    # initialize total counter
    total = 0.0
    # all conditions handling if dict1 or dict2 is in letter list and then performing the appropriate calculations after
    for individual_letters in letter_list:
        if individual_letters in dict1 and individual_letters in dict2:
            total -= dict1.get(individual_letters) * math.log2(dict2.get(individual_letters))
        if individual_letters in dict1 and individual_letters not in dict2:
            total -= dict1.get(individual_letters) * math.log2(minimum_freq2)
        if individual_letters not in dict1 and individual_letters in dict2:
            total -= minimum_freq1 * math.log2(dict2.get(individual_letters))

    return total


def guess_key(encrypted):

    # getting the english frequencies by reading the frank text file and then passing it through the get frequencies function
    # to get the frequency dictionary
    with open('frank.txt', 'r') as f:
        english_frequencies = get_frequencies(f.read())

    # this block is meant to split encrypyted into 3
    string_1 = ''
    string_2 = ''
    string_3 = ''
    for index, value in enumerate(encrypted):
        if index % 3 == 0:
            string_1 += value
        elif index % 3 == 1:
            string_2 += value
        else:
            string_3 += value

    # initialize three dictionaries to compare them
    min_1 = {}
    min_2 = {}
    min_3 = {}

    # iterates through the alphabet into getting the cross entropy for each letter and then putting them into their
    # own dictionary
    for letter in range(len(ALPHABET)):
        min_1[ALPHABET[letter]] = cross_entropy(english_frequencies, get_frequencies(decrypt(string_1, ALPHABET[letter])))
        min_2[ALPHABET[letter]] = cross_entropy(english_frequencies, get_frequencies(decrypt(string_2, ALPHABET[letter])))
        min_3[ALPHABET[letter]] = cross_entropy(english_frequencies, get_frequencies(decrypt(string_3, ALPHABET[letter])))

    # getting the minimum value for all the dictionaries
    min1_value = min(min_1, key=min_1.get)
    min2_value = min(min_2, key=min_2.get)
    min3_value = min(min_3, key=min_3.get)

    # stringing them together
    key = min1_value + min2_value + min3_value

    return str(key)


def crack(encrypted_text):
    # decrypt takes two parameters and one of them being the key so I pass through the guess key function to get the key
    # of the desired text
    final_message = decrypt(encrypted_text, guess_key(encrypted_text))
    return final_message




