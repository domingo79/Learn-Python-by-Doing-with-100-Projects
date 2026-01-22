"""
Analizziamo il testo inserito dall'utente:
- Total Characters:
- Total Words:
- Total Sentences:
- Most Frequent Word: 'and' (used 4 times)
- Avarage Word Lenght: 5.07 characters
- Avarage Sentence Lenght: 15.07 words
"""
text = input("Enter a block of text for analysis:\n")
characters = len(text)
words = len(text.split())
sentences = text.count(".") + text.count("?") + text.count("!")


def remuve_punctuaction(text):
    """Rimuove i caratteri speciali dal testo

    Args:
        text (str): testo inserito dall'utente

    Returns:
        str: testo ripulito senza punteggiatura
    """
    punctuation = ".,;:!?\"\”\‘\’«»\'\"()`-[]{}"
    for char in punctuation:
        text = text.replace(char, "")
    return text


word_frequency = {}
word_list = remuve_punctuaction(text).lower().split()

for word in word_list:
    if word not in word_frequency:
        word_frequency[word] = 1
    else:
        word_frequency[word] += 1

most_frequnt_word = max(word_frequency, key=word_frequency.get)

lenghts = [len(word) for word in word_list]
avarage_word_lenght = sum(lenghts) / len(lenghts)
avarage_sentence_lenght = words / sentences

print("Text Analysis Results:")
print("-" * 20)
print(f"Total Characters: {characters}")
print(f"Total Words: {words}")
print(f"Total Sentences: {sentences}")
print(
    f"Most Frequent Word: '{most_frequnt_word}' (used {word_frequency[most_frequnt_word]} times) ")
print(f"Avarage Word Lenght: {avarage_word_lenght:.2f} characters")
print(f"Avarage Sentence Lenght: {avarage_sentence_lenght:.2f} words)")
