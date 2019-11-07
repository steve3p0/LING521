# from nltk.corpus import PlaintextCorpusReader
# corpus_root = 'corpora/'  # Mac users should leave out C:
# corpus = PlaintextCorpusReader(corpus_root, '.*txt')  # all files ending in 'txt'
#

import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')
nltk.download('tagsets')
nltk.download('stopwords')

# tagset_upenn = nltk.help.upenn_tagset()
from nltk.corpus import stopwords

aux_verbs = ['be', 'am', 'are', 'is', 'was', 'were', 'being', 'been',
             'can', 'could', 'dare',
             'do', 'does', 'did',
             'have', 'has', 'had', 'having',
             'may', 'might', 'must', 'need', 'ought', 'shall', 'should', 'will', 'would']
coordinators = ['and', 'or', 'but', 'nor']

adverbs = ['then', 'why']

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

stops = set(stopwords.words("english"))

counter_list = []
for msg in messages:
    tokens = nltk.word_tokenize(msg)
    #print(tokens)
    pos = nltk.pos_tag(tokens, tagset='universal')
    print(f"\nmessage: {pos}")


    lstops = [x.lower() for x in stops]
    function_words = [word for word in tokens if word in lstops]
    fw_count = len(function_words)
    print(f"Function Words: {fw_count}")

    count = Counter([j for i,j in pos])
    counter_list.append(count)
    print(f"count: {count}")

counter_pos = sum(counter_list, Counter())
print(f"\nCounts: {counter_pos}")


N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()








