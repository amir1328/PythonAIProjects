import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

# Download necessary resources
nltk.download('punkt')

def summarize(text, num_sentences=3):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    
    # Count word frequency
    word_freq = Counter(words)
    
    # Score sentences based on word frequency
    sentence_scores = {sent: sum(word_freq[word] for word in word_tokenize(sent.lower()) if word in word_freq) for sent in sentences}
    
    # Select top sentences
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    
    return ' '.join(summary_sentences)

# Example Usage
text = """Artificial intelligence (AI) is intelligence demonstrated by machines, 
          as opposed to natural intelligence displayed by animals including humans. 
          AI research has been defined as the field of study of intelligent agents. 
          Some popular AI applications include machine learning, computer vision, and robotics. 
          AI is widely used in industries such as healthcare, finance, and automation."""
          
summary = summarize(text, num_sentences=2)
print(summary)
