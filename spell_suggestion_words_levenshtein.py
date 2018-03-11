import distance
import nltk

dict_words=nltk.corpus.words.words('en')

#print(dict_words)
sim_words = []
sim_dist = []

for word in dict_words:
    if distance.nlevenshtein(word, "applicablity", method=1) <= 0.25 :
        sim_words.append(word)
        sim_dist.append(distance.nlevenshtein(word, "applicablity", method=1))
        #print(word)


print(sim_words)
print(sim_dist)
min_value = min(sim_dist)
print(min_value)

index_min_val= sim_dist.index(min(sim_dist))

print(index_min_val)

print(sim_words[index_min_val])
