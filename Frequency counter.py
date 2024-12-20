
def count_words(sentence):
    
    from collections import Counter
    return Counter(sentence.lower().split())


sentence = input("Enter a sentence: ")


word_counts = count_words(sentence)
#co untd
for word, count in word_counts.items():
    print(f"{word}: {count}")








