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

FILE_URL = "https://frog.tips/api/1/tips"
SENTENCE_LENGTH = 50

response = requests.get(FILE_URL)
dict = json.loads(response.content)
item_nr = random.randint(0, len(dict['tips'])-1)
text = dict['tips'][item_nr]['tip']

phrase = []
length = 0
for word in text.split():
    length += len(word) + 1
    if length >= SENTENCE_LENGTH:
        phrase.append("\n       ")
        length = 0
    phrase.append(word)
    #print(phrase)

text = " ".join(phrase)



#print(item_nr)

frog = r"""

        {text}
         /
        /
  @..@
 (----)
( >__< )
^^ ~~ ^^
"""

print(frog.format(text=text))
