# -*- coding: utf-8 -*
from __future__ import unicode_literals


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
        result = []
        words = msg.upper().split()
        for word in words:
            # jar for collecting morse characters
            morse_ch = []
            for ch in word:
                # check if we know about this character
                if ch in self.allowed_characters:
                    morse_ch.append(self.alphabet[ch])
                # skip unknown characters
            if len(morse_ch) > 0:
                result.append(' '.join(morse_ch))
        return ' / '.join(result)

    def decode(self, msg):
        result = []
        words = msg.split('/')
        for word in words:
            morse_letters = word.split()
            letter = ''.join([self.inveresed_alphabet[l] for l in morse_letters])
            result.append(letter)
        return ' '.join(result)


