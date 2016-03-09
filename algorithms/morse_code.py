# -*- coding: utf-8 -*
from __future__ import unicode_literals
from string import ascii_letters, digits, whitespace


class MorseCode(object):

    def __init__(self):
        # International Morse Code Alphabet
        # http://morsecode.scphillips.com/morse2.html
        self.alphabet = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                         'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                         'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                         'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                         'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                         'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
                         '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                         '7': '--...', '8': '---..', '9': '----.', ',': '--..--',
                         ' ': '/'}
        self.inveresed_alphabet = dict((v, k) for (k, v) in self.alphabet.items())
        # we will encode only allowed characters
        self.allowed_characters = ''.join(ch for ch in self.alphabet.keys())

    def encode(self, msg):
        result = ''
        for ch in msg[:].upper():
            # check if we know about this character
            if ch in self.allowed_characters:
                print('## ', ch, self.alphabet[ch.upper()])
                result += self.alphabet[ch.upper()] + ' '
            # skip unknown characters
        return result

    def decode(self, msg):
        result = ''
        words = msg.split('/')
        for word in words:
            print("# decoding ", word)
            morse_letters = word.split()
            letter = ''.join([self.inveresed_alphabet[l] for l in morse_letters])
            result += ' ' + letter
        return result


