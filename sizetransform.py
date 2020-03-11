from bs4 import BeautifulSoup
import json
import nltk
import requests
from nltk import pos_tag, word_tokenize
import sys
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import recipeParser
from fractions import Fraction
import re

#Size transformation takes in recipe object

def checkIsInt(key):
  try:
    ind = int(key)
  except ValueError:
    return False
  return True

def checkIsFrac(val):
  try: 
    frac = Fraction(val)
  except ValueError:
    return False
  return True

_MIXED_FORMAT = re.compile(r"""
    \A\s*                      # optional whitespace at the start, then
    (?P<sign>[-+]?)            # an optional sign, then
    (?P<whole>\d+)             # integer part
    \s+                        # whitespace
    (?P<num>\d+)               # numerator
    /(?P<denom>\d+)            # denominator
    \s*\Z                      # and optional whitespace to finish
""", re.VERBOSE)

def mixed(s):
    """Parse the string s as a (possibly mixed) fraction.

        >>> mixed('1 2/3')
        Fraction(5, 3)
        >>> mixed(' -1 2/3 ')
        Fraction(-5, 3)
        >>> mixed('-0  12/15')
        Fraction(-4, 5)
        >>> mixed('+45/15')
        Fraction(3, 1)

    """
    m = _MIXED_FORMAT.match(s)
    if not m:
        return Fraction(s)
    d = m.groupdict()
    result = int(d['whole']) + Fraction(int(d['num']), int(d['denom']))
    if d['sign'] == '-':
        return -result
    else:
        return result

def doubleSize(recipeObject):
  for k in recipeObject:
    if checkIsInt(k):
      quant = recipeObject[k]['quantity']
      if checkIsInt(quant):
        quant = int(quant)
        recipeObject[k]['quantity'] = str(Fraction(quant * 2))  
      elif checkIsFrac(quant):
        quant = Fraction(quant)
        recipeObject[k]['quantity'] = str(Fraction(quant * 2))
      else: 
        quant = mixed(quant)
        recipeObject[k]['quantity'] = str(Fraction(quant * 2))
  return recipeObject

def halfSize(recipeObject):
  for k in recipeObject:
    if checkIsInt(k):
      quant = recipeObject[k]['quantity']
      if checkIsInt(quant):
        quant = int(quant)
        recipeObject[k]['quantity'] = str(Fraction(quant / 2))
      elif checkIsFrac(quant):
        quant = Fraction(quant)
        recipeObject[k]['quantity'] = str(Fraction(quant / 2))
      else:
        quant = mixed(quant)
        recipeObject[k]['quantity'] = str(Fraction(quant / 2))
  return recipeObject
