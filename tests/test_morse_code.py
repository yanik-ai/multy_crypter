from __future__ import unicode_literals

import unittest
from unittest import TestCase


from algorithms.morse_code import MorseCode


class MorseCodeTest(TestCase):

    def setUp(self):
        self.morse = MorseCode()

    def test_encrypt(self):
        """ Basic text encryption """
        plain_text = 'Abc 1230, %^&'
        cipher = '.- -... -.-. / .---- ..--- ...-- ----- --..--'
        self.assertEqual(cipher, self.morse.encode(plain_text))

    def test_decrypt(self):
        """ Basic text decryption """
        plain_text = 'Abc 1230,'
        cipher = '.- -... -.-. / .---- ..--- ...-- ----- --..--'
        self.assertEqual(plain_text.upper(), self.morse.decode(cipher))

    def test_encrypt_and_decrypt_full_alphabet(self):
        """
            Make sure no alphabet characters will be lost
            during encode/decode process
        """
        plain_text = ''.join(self.morse.alphabet.keys())
        cipher = self.morse.encode(plain_text)
        decoded_cipher = (self.morse.decode(cipher))
        self.assertEqual(plain_text, decoded_cipher)

    def test_encrypt_with_unknown_characters(self):
        """ Encoding should skip unknown characters """
        plain_text = 'This is Sparta!@#$%&*(),'
        # plain text except unknown characters
        clean_plain = ''.join(ch for ch in plain_text.upper() if ch in
                              self.morse.allowed_characters)
        plain_cipher = self.morse.encode(plain_text)
        clean_plain_cipher = self.morse.encode(clean_plain)
        self.assertEqual(plain_cipher, clean_plain_cipher)


if __name__ == '__main__':
    unittest.main()

