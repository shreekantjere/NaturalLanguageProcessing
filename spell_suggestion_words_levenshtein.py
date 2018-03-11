######Below code gives suggestion in a spell checker############

import nltk
import distance

#Array dict_words stores the words in english dictionary
dict_words=nltk.corpus.words.words('en')

#Array to store similar words
sim_words = []

#Array to store similarity values for each word in sim_words array
sim_dist = []


for word in dict_words:
    if distance.nlevenshtein(word, "applicablity", method=1) <= 0.25 :
        sim_words.append(word)
        sim_dist.append(distance.nlevenshtein(word, "applicablity", method=1))


#Minimum value among all the sim_dist values, which represents more similarity#
min_value = min(sim_dist)

#Extracting the index of the min_value
index_min_val= sim_dist.index(min(sim_dist))

#Suggeting word for wrong spelling
print(sim_words[index_min_val])