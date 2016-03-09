# -*- coding: utf-8 -*
from __future__ import unicode_literals
from string import whitespace

import unittest
from unittest import TestCase


from algorithms.caesar_cipher import CaesarCiphers


class CaesarCiphersTest(TestCase):

    def setUp(self):
        self.caesar = CaesarCiphers(steps=12)

    def test_encrypt(self):
        """ Basic text encryption """
        # plain = 'This is one small step for a man one giant leap for mankind'
        plain_text = 'This is one small step for a man one giant leap for mankind'
        cipher = 'FTUE UE AZQ EYMXX EFQB RAD M YMZ AZQ SUMZF XQMB RAD YMZWUZP'
        self.assertEqual(cipher, self.caesar.encode(plain_text))

    def test_decrypt(self):
        """ Basic text decryption """
        # plain = 'This is one small step for a man one giant leap for mankind'
        plain_text = 'This is one small step for a man one giant leap for mankind'
        cipher = 'FTUE UE AZQ EYMXX EFQB RAD M YMZ AZQ SUMZF XQMB RAD YMZWUZP'
        self.assertEqual(plain_text.upper(), self.caesar.decode(cipher))

    def test_encrypt_with_unknown_characters(self):
        """ Encoding should skip unknown characters """
        plain_text = 'This is Sparta!@#$%&*(),'
        plain_cipher = self.caesar.encode(plain_text)
        # plain text except unknown characters
        clean_plain = ''.join(ch for ch in plain_text if ch.upper() in self.caesar.allowed_characters + whitespace)
        clean_plain_cipher = self.caesar.encode(clean_plain)
        # make sure cleaned and contaminated encoding are the same
        self.assertEqual(plain_cipher, clean_plain_cipher)


if __name__ == '__main__':
    unittest.main()

