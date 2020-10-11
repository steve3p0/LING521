import nltk
#from nltk.tag.simplify import simplify_wsj_tag
from nltk.corpus import brown

nltk.download()

# Downloads
#nltk.download('universal_tagset')
# nltk.download()
#nltk.download('tagsets')
# nltk.download('averaged_perceptron_tagger')

messages = ["'Your books have sold millions of copies,' the young interviewer was saying.",
            'According to Kant and Laplace, the original mass of gas cooled and began to contract.',
            "The minibar was filled with candy, mineral water, decaffeinated soft drinks and dairy products. " \
            "'These are the kind of munchies which our research found helps sleep,' said Jeremy Baka, Hilton spokesman.",
            'You guys can go to a whole bunch of places and you should not go to New Mexico.' ]

tagset_upenn = nltk.help.upenn_tagset()
print(tagset_upenn)

pos_list = []
for msg in messages:
    tokens = nltk.word_tokenize(msg)
    #pos = nltk.pos_tag(tokens, tagset='universal')
    pos = nltk.pos_tag(tokens)
    #pos = tag_set.pos_tag(tokens, )
    #pos_simple = nltk.classify.
    print(pos)
    pos_list.append(pos)

#print(pos_list)

