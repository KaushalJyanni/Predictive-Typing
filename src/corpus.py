from collections import Counter
from collections import defaultdict
from sets import Set
import abc

class Corpus:

    DEFAULT_PROB = 0.0
    BOS = "<s>"
    EOS = "</s>"

    def __init__(self, max_n):
        self.max_n = max_n
        self.total_number_of_words = 0

        # how many ngrams there is in corpus
        self.all_n_grams = {}
        # which word continues me(ngram)
        self.n_gram_to_word = {}
        # set of all ngrams to which I continue
        self.word_to_ngram = {}

        for i in range(self.max_n):
            n = i + 1
            self.n_gram_to_word[n] = defaultdict(Counter)
            self.word_to_ngram[n] = defaultdict(set)
            self.all_n_grams[n] = set()

    def get_ngram_count(self, n, ngram, word):
        return self.n_gram_to_word[n][ngram][word]

    def get_unique_words(self):
        return self.all_n_grams[1]

    def get_total_number_of_words(self):
        return self.total_number_of_words

    def get_prefix_count(self, n, ngram):
        return sum(self.n_gram_to_word[n][ngram].values())

    def get_next_word(self, ngram, current_word=None):
        probabilities = []
        words = self.get_unique_words()

        for word in words:
            # because words are tuples
            word = word[0]
            # print word
            prob = self.get_word_probability(ngram, word)
            probabilities.append((word, prob))

        max_prob = 0
        predicted_word = "<Can't find a word>"
        for i in probabilities:
            if i[1] > max_prob:
                print current_word
                if current_word:
                    current_word_length = len(current_word)
                    if current_word == i[0][:current_word_length]:
                        max_prob = i[1]
                        predicted_word = i[0]
                else:
                    max_prob = i[1]
                    predicted_word = i[0]

        return predicted_word

    # @abc.abstractmethod
    # def get_word_probability(self, ngram, word):
    #     pass

    def train(self, input_file, discount=0.75):
        self.discount = discount
        total_sentences=0
        for sentence in input_file:
            # sentence format is "<s> word ... word </s>"
            total_sentences+=1
            words = sentence.split()
            self.total_number_of_words += len(words)

            for i in range(self.max_n):
                n = i + 1
                ngram = (self.BOS, ) * (n - 1)

                for word in words:
                    self.n_gram_to_word[n][ngram][word] += 1
                    self.all_n_grams[n].add(ngram + (word, ))
                    self.word_to_ngram[n][word].add(ngram)
                    if len(ngram) > 0:
                        ngram = ngram[1:] + (word,)
                # print "for n = ",n
                # print "map", self.all_n_grams
                # print "count map, ",self.n_gram_to_word
                # print
                # print "count map, 0,",self.n_gram_to_word[1]
                # print
                # print "continuation hello, ",self.word_to_ngram[n]['Hello']
                # print "continuation what, ",self.word_to_ngram[n]['what']
                # print
                # print
        print total_sentences
# with open("file.txt",'r') as f:
#     train(f)


