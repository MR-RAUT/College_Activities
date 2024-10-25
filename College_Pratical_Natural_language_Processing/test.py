# # 1 Convert the text into tokens. Find the word frequency.

# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.probability import FreqDist

# # Sample text
# text = """
# Convert the text into tokens. Find the word frequency.
# My name in Mahesh Raut
# """

# # Tokenize the text using nltk
# tokens = word_tokenize(text.lower())

# # Find the word frequency using FreqDist
# word_freq = FreqDist(tokens)

# # Output the tokens and word frequencies
# print("Tokens:", tokens)
# print("\nWord Frequency:")
# for word, freq in word_freq.items():
#     print(f"{word}: {freq}")

# # 2 Find the synonym /antonym of a word using WordNet.

# import nltk
# nltk.download('wordnet')

# from nltk.corpus import wordnet

# def get_synonyms_antonyms(word):
#     synonyms = []
#     antonyms = []

#     for syn in wordnet.synsets(word):
#         for lemma in syn.lemmas():
#             synonyms.append(lemma.name())
#             if lemma.antonyms():  # If antonyms exist
#                 antonyms.append(lemma.antonyms()[0].name())

#     return set(synonyms), set(antonyms)


# word = "happy"  # Replace with your word
# synonyms, antonyms = get_synonyms_antonyms(word)

# print(f"Synonyms of {word}: {synonyms}")
# print(f"Antonyms of {word}: {antonyms}")


# 3 Demonstrate a bigram/trigram language model. Generate regular expression for a given text
# 4 Perform Lemmatization and Stemming. Identify parts-of Speech using Penn Treebank tag set.
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag

# Download necessary corpora
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Sample text
text = "The quick brown foxes are jumping over the lazy dogs."

# Tokenize the text into words
tokens = word_tokenize(text)

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Perform stemming and lemmatization
stemmed_words = [stemmer.stem(token) for token in tokens]
lemmatized_words = [lemmatizer.lemmatize(token) for token in tokens]

# Perform POS tagging
pos_tags = pos_tag(tokens)

# Display results
print("Original Text:", tokens)
print("Stemmed Words:", stemmed_words)
print("Lemmatized Words:", lemmatized_words)
print("\nParts of Speech:")
for word, tag in pos_tags:
    print(f"{word}: {tag}")
