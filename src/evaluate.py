from corpus import *
from witten_bell import *
from kneser_ney import *

import sys
import math
# import codecs

def total_words(filename):
    count=0   
    with open(evaluate,'r') as f:
        data=f.readlines()
    for line in data:
        count+=len(line.split()[1:-1]) 
    return count

def calculate(smooth, ngram, train_set, eval_set):
    prob = 1.0
    entropy = 0.0
    perplexity = 0.0

    n = ngram - 1

    with open(train_set,'r') as f:
        smooth.train(f)

    tot_words = total_words(eval_set)

    probabilities = list()

    with open (eval_set,'r') as f:
        data = f.readlines()

    for line in data:
        sentence_probability=0
        s_prob = 1.0

        words = line.split()[1:-1]

        if(len(words) < ngram):
            continue

        for i in range(len(words) - n):
            context = tuple(words[i:i + n])
            word = words[i + n]
            word_probability = smooth.get_word_probability(context, word)
            if(float(word_probability)==0.0):
                word_probability=float(1)/tot_words
                # print "value",word_probability
            sentence_probability += math.log(word_probability,2)

        probabilities.append(sentence_probability)

    total = sum(probabilities)
    # print probabilities
    for p in probabilities:
        if (p) > 0.0:
            prob *= p

    entropy = -1.0 / tot_words * total
    perplexity = 2 ** entropy

    print "\tProbability = ", prob
    print "\tEntropy = ", entropy
    print "\tPerplexity = ", perplexity


training = sys.argv[1] # "../common/corpus_t.txt"
evaluate = sys.argv[2] # "../common/corpus_e.txt"

print "Training corpus: ", training
print "Evaluating on  : ", evaluate
# print total_words(evaluate)
print "Kneser Ney, n = 2"
calculate(KneserNey(4), 2, training, evaluate)

print "Witten Bell, n = 2"
calculate(Witten_Bell(4), 2, training, evaluate)

print "Kneser Ney, n = 3"
calculate(KneserNey(4), 3, training, evaluate)

print "Witten Bell, n = 3"
calculate(Witten_Bell(4), 3, training, evaluate)

print "Kneser Ney, n = 4"
calculate(KneserNey(4), 4, training, evaluate)

print "Witten Bell, n = 4"
calculate(Witten_Bell(4), 4, training, evaluate)

