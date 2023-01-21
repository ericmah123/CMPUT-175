from random import choice
from collections.abc import MutableSet


class TooShortError(ValueError):
    pass


class TooLongError(ValueError):
    pass


class NotLettersError(ValueError):
    pass


class WordleWords(MutableSet):
    """
    This class is for everything having to do with the words themselves. Things like making sure the word is valid and loading file
    """
    def __init__(self, letters):
        """
        Initializing function that makes words use the mutable set and initializing letters so it can be used throughout the class
        """
        self._letters = letters
        self._words = set()

    def __contains__(self, word):
        return word in self._words

    def __iter__(self):
        return iter(self._words)

    def __len__(self):
        return len(self._words)

    def add(self, word):
        if not self.check_word(word):
            self._words.add(word)

    def discard(self, word):
        self._words.discard(word)

    def load_file(self, filename):
        """
        loads file by opening and only adding words that are sufficient length to the set

        """
        with open(filename, 'r') as f:
            # iterates through the file
            for individual_word in f:
                # strips the white space
                final_word = individual_word.strip('\n')
                # making sure words that are added are proper size
                if len(final_word) == self._letters:
                    self._words.add(final_word)

    def check_word(self, word):
        """
        To ensure that word is up to proper specifications
        """
        if not word.isalpha():
            raise NotLettersError('Not in alphabet!')
        elif len(word) < self._letters:
            raise TooShortError('Word is too short!')
        elif len(word) > self._letters:
            raise TooLongError('Word is too long!')

    def letters(self):
        return len(self._words)

    def copy(self):
        """
        Returns a second WordleWords instance

        """
        new = WordleWords(self._letters)
        for individual_letters in self._words:
            new.add(individual_letters)
        return new


class Guess:
    """
    This class handles some of the gameplay mechanics. Handling things like a correct word, misplaced or if the word is incorrect
    """
    def __init__(self, guess, answer):
        """
        Initializing variables to be used

        """
        self._guess = guess
        self._answer = answer

    def guess(self):
        return self._guess

    def correct(self):
        """
        Iterate through answer and checking that if the index of answer equals guess then we count that as a correct word

        """
        correct_string = ''
        # enumerate to get index of each letter
        for letter_index, letter in enumerate(self._answer):
            # if they are in the same position add to the string, if not then add underscores
            if self._answer[letter_index] == self._guess[letter_index]:
                correct_string += letter
            else:
                correct_string += '_'

        return correct_string

    def misplaced(self):
        """
        Checks that the letter is in the guess but not at the same position

        """
        misplaced_string = ''
        # enumerate to get index of each letter
        for letter_index, letter in enumerate(self._answer):
            # ensure that letter is in word but is in the wrong position
            if letter in self._guess and not self._answer[letter_index] == self._guess[letter_index]:
                misplaced_string += letter

        return misplaced_string

    def wrong(self):
        """
        Takes every letter that is not in the answer and puts it in a sorted string
        """
        copy_ans = [letter for letter in self._answer]
        final_string = []
        for letter in self._guess:
            if letter in copy_ans:
                copy_ans.remove(letter)
            else:
                final_string.append(letter)

        string_sorted = sorted(final_string)
        empty_space = ''
        complete_string = empty_space.join(string_sorted)
        return complete_string

    def is_win(self):
        return self._guess == self._answer


class Wordle:
    """
    Final touches to the game. Keeps track of guesses and handles other things like getting a random word
    """
    def __init__(self, words):
        """
        Initializes variables to be used
        """
        self._words = words
        self._guess = 0
        converted_set = list(words)
        self._random = choice(converted_set)

    def guesses(self):
        return self._guess

    def guess(self, guessed):
        """
        It will increment each time this function is called
        """
        guessed_word = Guess(guessed, self._random)
        self._guess += 1
        return guessed_word
