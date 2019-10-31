# from nltk.corpus import PlaintextCorpusReader
# corpus_root = 'corpora/'  # Mac users should leave out C:
# corpus = PlaintextCorpusReader(corpus_root, '.*txt')  # all files ending in 'txt'
#

import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('universal_tagset')
nltk.download('tagsets')
# tagset_upenn = nltk.help.upenn_tagset()

messages = ['Gym?',
            'yeah be there in about a half',
            'Ok see you when you get here!',
            'Seconds away',
            'Meet me between smith and cramer asap',
            'I got you and Taylor tix in pit section.',
            'Get some milk please',
            'Chk email',
            'Made it',
            'Do u know where u saved that movie on my compute',
            'Im meeting some dude from the internet for happy hour ahh!',
            'Wed is dinner for renetta call us soon',
            'where r u???',
            'pinball']

counter_list = []
for msg in messages:
    tokens = nltk.word_tokenize(msg)
    #print(tokens)
    pos = nltk.pos_tag(tokens, tagset='universal')
    #print(pos)

    count = Counter([j for i,j in pos])
    counter_list.append(count)
    #print(count)

counter_pos = sum(counter_list, Counter())
print(counter_pos)









