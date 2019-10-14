import nltk
#from nltk.tag.simplify import simplify_wsj_tag
#from nltk.corpus import brown

# Downloads
nltk.download('universal_tagset')
# nltk.download()
#nltk.download('tagsets')
# nltk.download('averaged_perceptron_tagger')
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

tag_set = nltk.help.upenn_tagset()
#tag_set2 = nltk.tagset_mapping()
print(tag_set)

for msg in messages:
    tokens = nltk.word_tokenize(msg)
    pos = nltk.pos_tag(tokens, tagset='universal')
    #pos_simple = nltk.classify.
    print(pos)


# wordtags = nltk.ConditionalFreqDist((w.lower(), t)
#         for w, t in nltk.corpus.brown.tagged_words(tagset="universal"))
# #print(wordtags["report"])
# #FreqDist({'NOUN': 135, 'VERB': 39})
# kind = list(wordtags["kind"])

class BackoffTagger:
    def __init__(self):
        self._taggers = [nltk.PerceptronTagger()]

model = {'example_one': 'VB', 'example_two': 'NN'}
tagger = nltk.tag.UnigramTagger(model=model, backoff=BackoffTagger())
tagger.tag(['example_one'])



print('the end')
#['ADJ', 'NOUN']