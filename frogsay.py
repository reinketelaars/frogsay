#!/usr/bin/env python3
#
# Geïnspireerd door: https://puppet.com/blog/deploy-packages-across-your-windows-estate-with-bolt-and-chocolatey/
#
# ... maar kon 'frogsay' niet vinden in apt.
# 2020-01-26
#
# ...of toch wel in PyPi...
# ...maar werkt niet met oudere versie van requests? (2.21)
#

import requests
import json
import random
import sys

FILE_URL = "https://frog.tips/api/1/tips"
SENTENCE_LENGTH = 50

class Frog():
    """The revised and simplified version of frogsay.
    It retrieves tips from the frog.tips website, 
    prints an ASCII frog that speaks the random tip.
    """
    def __init__(self):
        pass

    def get_tips(self):
        """Retrieves tips from the site and randomly selects one."""
        # get data from site
        response = requests.get(FILE_URL)
        # get content from site into variable 'dict' as a dictionary
        dict = json.loads(response.content)
        # choose a random tip. Only key is 'tips'. Value is entire list of tips.
        # in the format: list of dictionaries with two keys each ('tip' en 'number')
        text = random.choice(list(dict['tips']))['tip']
        # text is a string
        return text

    def speak(self, text):
        """Prints an ASCII frog including tha random tip.

        Takes a tip as argument as a string."""
        phrase = []
        length = 0
        for word in text.split():
            # Increase length with the length of each word + space.
            length += len(word) + 1
            # if length is longer than desired: add a line break
            if length >= SENTENCE_LENGTH:
                phrase.append("\n      ")
                length = 0
            phrase.append(word)

        # join the list of words (and line breaks) into a new string.
        text = " ".join(phrase)

        frog = r"""
       {text}
        /
       /
  @..@
 (----)
( >__< )
^^ ~~ ^^ """

        print(frog.format(text=text))
        return 0

def main():
    frog = Frog()
    text = frog.get_tips()
    sys.exit(frog.speak(text))

if __name__ == '__main__':
    main()

