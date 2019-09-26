# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
import numpy as np
import requests

setList = np.genfromtxt(r'20190926.txt')

session = requests.Session()

pieces = 0
unfound = 0
sets = len(setList)
for i, st in enumerate(setList):
    resp = session.get(f'https://brickset.com/sets/{int(st)}-1')
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text)
        # There must be a better way for this
        idx = 0
        for elem in soup.find_all('dt'):
            if elem.text == 'Pieces':
                break
            else:
                idx += 1
        pieces += int(soup.find_all('dd')[idx].text)
        print(f'Processing {i+1} of {sets}', end="\r", flush=True)
    else:
        unfound += 1

print(f'Total number of pieces owned {pieces}.')
if unfound > 0:
    print(f"I couldn't find {unfound} sets on Brickset")
