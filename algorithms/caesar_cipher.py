# -*- coding: utf-8 -*
from __future__ import unicode_literals
from string import whitespace

import unittest


class CaesarCiphers(object):
    """
    Cesar Ciphers encryption/decryption approach.
    """

    def __init__(self, steps=12):
        self.alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
                         'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
                         'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
        self.inveresed_alphabet = dict((v, k) for (k, v) in self.alphabet.items())
        self.allowed_characters = ''.join(ch for ch in self.alphabet.keys())
        self.alphabet_len = len(self.alphabet)
        self.steps = steps

    def encode(self, msg):
        """
            Encode giving message by shifting character to right
            for number of giving steps
        """
        result = ''
        for ch in msg.upper():
            if ch in self.allowed_characters:
                i = (self.alphabet[ch.upper()] + self.steps) % self.alphabet_len
                result += self.inveresed_alphabet[i]
            elif ch in whitespace:
                # no need to encode whitespaces
                result += ch
        return result

    def decode(self, msg):
        """
            Decode giving message by shifting character to right
            for number of giving steps
        """
        result = ''
        for ch in msg:
            if ch in whitespace:
                # no need to decode whitespaces
                result += ch
            else:
                i = (self.alphabet[ch.upper()] - self.steps) % self.alphabet_len
                result += self.inveresed_alphabet[i]
        return result


if __name__ == '__main__':
    unittest.main()
