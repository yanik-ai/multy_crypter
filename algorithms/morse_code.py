# -*- coding: utf-8 -*
from __future__ import unicode_literals
from string import ascii_letters, digits, whitespace


class MorseCode(object):

    def __init__(self):
        # init alphabet and reversed alphabet
        self.alphabet = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                         'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                         'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                         'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                         'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                         'Y': '-.--', 'Z': '--..', ' ': '−···−', '0': '-----',
                         '1': '.----',  '2': '..---', '3': '...--', '4': '....-',
                         '5': '.....', '6': '-....',  '7': '--...',  '8': '---..',
                         '9': '----.'
                         }
        self.inveresed_alphabet = dict((v, k) for (k, v) in self.alphabet.items())
        # we will encode only allowed characters
        self.allowed_characters = ascii_letters + digits + whitespace

    def encode(self, msg):
        result = ''
        for ch in msg[:]:
            # check if we know about this character
            if ch in self.allowed_characters:
                result += self.alphabet[ch.upper()] + ' '
            # skip unknown characters
        return result

    def decode(self, msg, pos=0):
        if pos < len(msg):
            morse_letter = ''
            for key, ch in enumerate(msg[pos:]):
                if ch == ' ':
                    pos = key + pos + 1
                    letter = self.inveresed_alphabet[morse_letter]
                    return letter + self.decode(msg, pos)
                else:
                    morse_letter += ch
        else:
            return ''
