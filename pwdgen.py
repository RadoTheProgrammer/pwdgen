"""
A simple password generator
"""


import secrets
CONSONANTS = "bcdfghjklmnpqrstvwxz"
VOWELS = "aeiouy"
SPECIAL_CHARS=".:;-!&*_+#,=" # #!$%^&*

def generate(syllables=6):
    pw = ""
    for _ in range(syllables):
        pw += secrets.choice(CONSONANTS) + secrets.choice(VOWELS)
        
    idx_sep = (secrets.randbelow(syllables)+1)*2
    pw = pw[:idx_sep].capitalize() + secrets.choice(SPECIAL_CHARS) + pw[idx_sep:].capitalize()
    
    number=str(secrets.randbelow(10))
    if secrets.randbelow(2):
        pw+=number
    else:
        pw=number+pw
    return pw

def main():
    import argparse
    parser = argparse.ArgumentParser(description="A simple password generator")
    parser.add_argument("-s","--syllables", type=int, default=6, help="Number of syllables in the password")
    parser.add_argument("number", type=int, default=1, nargs='?', help="Number of passwords to generate")
    args = parser.parse_args()
    for _ in range(args.number):
        print(generate(args.syllables))