import unittest

from translator import englishtofrench, frenchtoenglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtofrench('hello'), 'bonjour')#test when 'Hello' is given as input and 'Bonjour' is given as output

class TestFrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello')#test when 'Bonjour' is given as input and 'Hello' is given as output
        
unittest.main()
