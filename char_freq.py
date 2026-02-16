word="mammal"
freq={}
for char in word:
    freq[char]=freq.get(char,0)+1
print(freq)