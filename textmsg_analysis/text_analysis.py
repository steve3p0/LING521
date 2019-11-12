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
from collections import defaultdict

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

sentence_lengths = [len(sentence.split()) for sentence in messages]
total_words = sum(sentence_lengths)
print(f"Sentence Lengths: {sentence_lengths}")
print(f"Grand Total Words: {total_words}")

insert_words = [ 'yeah', 'Ok', 'ahh' ]
stops = set(stopwords.words("english"))

counter_list = []
words = defaultdict(list)
for msg in messages:
    tokens = nltk.word_tokenize(msg)
    #print(tokens)
    word_tag_pairs = nltk.pos_tag(tokens, tagset='universal')
    print(f"\nRaw Message: {msg}")
    print(f"POS: {word_tag_pairs}")

    for w, tag in word_tag_pairs:
        words[tag].append(w)

    lstops = [x.lower() for x in stops]
    function_words = [word for word in tokens if word in lstops]
    fw_count = len(function_words)
    words['FW'].extend(function_words)
    print(f"Function Words (Stop Words): {function_words}")
    print(f"Function Word Count: {fw_count}")

    count = Counter([j for i,j in word_tag_pairs])
    count['FW'] = fw_count
    counter_list.append(count)
    print(f"POS Count: {count}")

counter_pos = sum(counter_list, Counter())
print(f"\nSummary - POS Tagging")
print(f"counter_pos: {counter_pos}")
print(f"Nouns: {words['NOUN']}")
print(f"Verbs: {words['VERB']}")
print(f"Adjectives: {words['ADJ']}")
print(f"Adverbs: {words['ADV']}")
print(f"Function Words: {words['FW']}")
print(f"Inserts: {words['Inserts']}")

# Counts
#counter_static = Counter({'NOUN': 29, 'VERB': 12, 'ADP': 9, 'ADV': 8, 'PRON': 8, '.': 7, 'DET': 4, 'ADJ': 3, 'CONJ': 2})
raw_counts_nouns = counter_pos['NOUN']
raw_counts_verbs = counter_pos['VERB']
raw_counts_adverbs = counter_pos['ADV']
raw_counts_adjectives = counter_pos['ADJ']
raw_counts_functors = counter_pos['FW']
raw_counts_inserts = counter_pos['Inserts']

percent_nouns = raw_counts_nouns / total_words
percent_verbs = raw_counts_verbs / total_words
percent_adjectives = raw_counts_adjectives / total_words
percent_adverbs = raw_counts_adverbs / total_words
percent_functors = raw_counts_functors / total_words
percent_inserts = raw_counts_inserts / total_words

norm_counts_nouns = percent_nouns * 1000
norm_counts_verbs = percent_verbs * 1000
norm_counts_adjectives = percent_adjectives * 1000
norm_counts_adverbs = percent_verbs * 1000
norm_counts_functors = percent_functors * 1000
norm_counts_inserts = percent_inserts * 1000

print(f"\nRaw Counts:")
print(f"Nouns: {raw_counts_nouns}")
print(f"Verbs: {raw_counts_verbs}")
print(f"Adjectives: {raw_counts_adjectives}")
print(f"Adverbs: {raw_counts_adverbs}")
print(f"Function Words: {raw_counts_functors}")
print(f"Inserts: {raw_counts_inserts}")

print(f"\nPercentages:")
print(f"Nouns: {percent_nouns:.1%}")
print(f"Verbs: {percent_verbs:.1%}")
print(f"Adjectives: {percent_adjectives:.1%}")
print(f"Adverbs: {percent_adverbs:.1%}")
print(f"Function Words: {percent_functors:.1%}")
print(f"Inserts: {percent_inserts:.1%}")

print(f"\nNormed Counts Per 1000:")
print(f"Nouns: {norm_counts_nouns:0.1f}")
print(f"Verbs: {raw_counts_verbs:0.1f}")
print(f"Adjectives: {norm_counts_adjectives:0.1f}")
print(f"Adverbs: {norm_counts_adverbs:0.1f}")
print(f"Function Words: {norm_counts_functors:0.1f}")
print(f"Inserts: {norm_counts_inserts:0.1f}")

# Graphing
width = 0.7
p1 = plt.bar(width=width, x=1, height=norm_counts_nouns)
p2 = plt.bar(width=width, x=1, height=norm_counts_verbs, bottom=norm_counts_nouns)
p3 = plt.bar(width=width, x=1, height=norm_counts_adverbs, bottom=norm_counts_nouns + norm_counts_verbs)
p4 = plt.bar(width=width, x=1, height=norm_counts_adjectives, bottom=norm_counts_nouns + norm_counts_verbs + norm_counts_adverbs)

plt.ylabel('Normed Counts Per 1000 Words')
plt.title('2007 Text Messages: Frequency of Lexical Word Classes')
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off

actual_last_value = norm_counts_nouns + norm_counts_verbs + norm_counts_adverbs
max_y_value = total_words * 1000
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), handles=(p1[0], p2[0], p3[0], p4[0]), labels=('Nouns', 'Verbs', 'Adverbs', 'Adjectives'))
plt.autoscale(False)
plt.show()
