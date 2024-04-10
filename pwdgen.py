"""
A simple password generator
"""


import random
CONSONANTS = "bcdfghjklmnpqrstvwxz"
VOWELS = "aeiouy"
SPECIAL_CHARS=".:;-!&*_+#,=" # #!$%^&*

def generate(syllables=6):
    pw = ""
    for _ in range(syllables):
        pw += random.choice(CONSONANTS) + random.choice(VOWELS)
        
    idx_sep = random.randrange(1,syllables)*2
    pw = pw[:idx_sep].capitalize() + random.choice(SPECIAL_CHARS) + pw[idx_sep:].capitalize()
    
    number=str(random.randrange(10))
    if random.randrange(2):
        pw+=number
    else:
        pw=number+pw
    return pw