
word = input("Enter a word: ")
vowels = ['a', 'e', 'i', 'o', 'u']
exempt = ['s', 'd']
syllables = []
word_len = len(word)
i = 0
while i < word_len:
    char = word[i]

    # If the current character is the last character
    if i + 1 == word_len:

        # Do not count final -e, except for -le
        if (char == 'e') and (word[i - 1] == 'l'):
            syllables.append(char)
        elif (char in vowels) and (char != 'e'):
            syllables.append(char)
        i += 1

    # If the current character is not the last character
    else:

        # If the current character is a vowel
        if char in vowels:

            # If the vowel is 'e' and the 2nd to the last letter in the word
            if (char == 'e') and (i + 2 == word_len):
                if (word[i + 1] == 's') or (word[i + 1] == 'd'):
                    i += 2
                else:
                    syllables.append(char)
                    i += 1
            # If the vowel has another vowel after it
            elif word[i + 1] in vowels:
                syllables.append(char)
                i += 2
            # If the vowel has a consonant after it
            else:
                syllables.append(char)
                i += 1
        else:
            i += 1
    

print("Number of syllables: %d" % len(syllables))          

