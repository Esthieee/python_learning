vowels = ['a', 'e', 'i', 'o', 'u']
word = input('输一个英文单词:')
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowels in found:
    print(vowels)