"""
this code translates english to french and vice versa
The functions in this module include:
- englishtofrench(englishtext): translates english to french.
- frenchtoenglish(frenchtext): translates french to english.
"""
from deep_translator import MyMemoryTranslator

def englishtofrench(englishtext):
    """
    this function translates english to french
    """
    frenchtext = MyMemoryTranslator(source = 'english', target = 'french').translate(englishtext)
    return frenchtext

def frenchtoenglish(frenchtext):
    """
    this function tranlates french to english 
    """
    englishtext = MyMemoryTranslator(source = 'french', target = 'english').translate(frenchtext)
    return englishtext
    