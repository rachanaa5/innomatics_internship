sentence="I am an intern at Innomatics Research labs"
def unique_words(sentence):
    words=sentence.split()
    unique=set(words)
    return unique
print(unique_words(sentence))
print(f"total unique words :{len(unique_words(sentence))}")
