'''
    IS72727 - Cordero Hernández, Marco Ricardo
    Cloud Architecture Project
    URL Shortener
'''
import re
from random import random, choice
from string import ascii_lowercase, ascii_letters
nums = list(map(str, range(10)))

def getRandBits(length: int = 2) -> str:
    ''' Random components of shortened URL '''
    bits = []

    for i in range(length):
        bits.append(choice(ascii_lowercase if (i % 2 == 0) else nums))

    return ''.join(bits)

def removeHead(url: str) -> str:
    ''' Remove protocol and www from url '''
    pattern = r'^(?:http[s]?:\/{2})?(.*?\.)(.*)$'
    search = re.search(pattern, url)

    if (search):
        if (search.group(1).startswith('http')):
            return ''

        if (search.group(1) == 'www.'):
            return search.group(2)
        return ''.join(search.groups())
    return

def shortener(url: str, short_length: int = 10) -> str:
    ''' Shorten url '''
    if (len(url) > 200 or not (url := removeHead(url))): # Invalid URL or too long
        return ''
    
    print(url)
    i = 0
    short_url = ''
    order = True if (int(random()*10) % 2 == 0) else False

    while (len(short_url) != short_length - 2 and i != len(url)):
        holder = ord(url[i if order else len(url)-i-1].lower())

        if (97 <= holder <= 122): # Letter
            if (holder != 122): # Z case
                short_url += choice(ascii_lowercase)
            else:
                short_url += chr(holder + 1)
        elif (holder in nums): # Number
            short_url += ascii_lowercase[(int(holder) + 13) % len(ascii_lowercase)]
        
        i += 1
    
    return short_url + getRandBits(length=short_length-len(short_url))

# def urlShortener()

if __name__ == '__main__':
    # TODO: Consider handling url length and format outside shortener function
    #       as the current system it's confusing
    
    test = 'https://iteso.instructure.com/courses/32932'
    print(shortener(test))
