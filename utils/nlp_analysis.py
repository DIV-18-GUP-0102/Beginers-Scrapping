import re
import nltk
import string
import syllapy
from nltk.tokenize import sent_tokenize, word_tokenize

def perform_nlp_analysis(text_content):
    # Tokenized sentences
    sentences = sent_tokenize(text_content)
    words = []
    total_words = 0

    for sentence in sentences:
        # Removing punctuation marks from the sentences
        cleaned_sentence = sentence.translate(str.maketrans('', '', string.punctuation))

        sentence_words = word_tokenize(cleaned_sentence)

        words.extend(sentence_words)

        word_count = len(sentence_words)
        total_words += word_count


    # Counting Personal Pronouns
    personal_pronouns = ["I", "we", "my", "ours", "us"]

    # Constructing the regex pattern to match any of the personal pronouns
    pattern = r'\b(?:' + '|'.join(re.escape(pronoun) for pronoun in personal_pronouns if pronoun != "US") + r')\b'

    # Finding all matches of personal pronouns in the text content
    matches = re.findall(pattern, text_content, flags=re.IGNORECASE)

    # The count of personal pronouns (excluding "US")
    personal_pronoun_count = len(matches)

    # Calculating average word count per sentence
    average_word_per_sentence = total_words / len(sentences)   
    unique_words = list(set(words))

    # Calculating average word length
    total_length = sum(len(word) for word in unique_words)
    avg_word_length = total_length/len(unique_words)


    # The average sentence length
    num_sentences = len(sentences)
    num_words = len(words)
    # print(num_words)
    # print(words)
    avg_sentence_length = num_words / num_sentences
    
    # Removing Proper Nouns
    stopwords_file = "utils/ProperNoun.txt"  
    with open(stopwords_file, 'r', encoding='utf-8') as file:
        stopwords = [line.strip().lower() for line in file]
    # Filtered words after excluding the words found in the provided 13416 Proper noun list 
    filtered_words = [word for word in words if word.lower() not in stopwords]

    # Total Syllables from each word
    # Counting the complex words including duplicates
    complex_word = 0
    syllable_counts = 0
    complex_words = []

    for word in filtered_words:
        syllables = syllapy.count(word)
        syllable_counts = syllable_counts + syllables
        if syllables > 2:
            complex_word += 1
            complex_words.append(word)

    # Syllable per word
    syllable_counts = syllable_counts/len(filtered_words)
    # Complex Word Percentage
    complex_words_percentage = complex_word / num_words
    # Gunning Fog Index
    Fog_Index = 0.4 * (avg_sentence_length + complex_words_percentage)

    # Complex word count
    unique_complex_word = list(set(complex_words))
    complex_word_count = len(unique_complex_word)

    # Removing generic Nouns
    stopwords_file = "utils/generic.txt"  
    with open(stopwords_file, 'r', encoding='utf-8') as file:
        stopwords = [line.strip().lower() for line in file]
    # Filtered words after excluding the words found in the provided 13416 Proper noun list 
    filtered_words_2 = [word for word in filtered_words if word.lower() not in stopwords]


    # Load positive and negative word lists
    positive_file = "utils/positive.txt"
    negative_file = "utils/negative.txt"
    with open(positive_file, 'r') as f:
        positive_words = set(word.strip() for word in f.readlines())
    with open(negative_file, 'r') as f:
        negative_words = set(word.strip() for word in f.readlines())

    # Count occurrences of positive and negative words
    positive_score = sum(1 for word in filtered_words_2 if word in positive_words)
    negative_score = sum(1 for word in filtered_words_2 if word in negative_words)

    # Calculate Polarity Score
    polarity_score = (positive_score - negative_score) / (positive_score + negative_score + 0.000001)

    # Calculate Subjectivity Score
    total_words = len(filtered_words_2)
    subjectivity_score = (positive_score + negative_score) / (total_words + 0.000001)

    # Word count
    word_count = len(filtered_words_2)

    return positive_score, negative_score, polarity_score, subjectivity_score, avg_sentence_length, complex_words_percentage, Fog_Index, average_word_per_sentence, complex_word_count, word_count, syllable_counts, personal_pronoun_count, avg_word_length


               
    
    
    
    

