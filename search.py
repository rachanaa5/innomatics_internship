query="Online mobile shopping buy mobile online"
words=query.lower().split()
frequency={}
for word in words:
    frequency[word]=frequency.get(word,0)+1
duplicate_words={k: v for k, v in frequency.items()if v>1}
print(duplicate_words)