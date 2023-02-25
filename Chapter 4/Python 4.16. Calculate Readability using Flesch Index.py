"""
Python Exercise 4.16
Written by: Iam Rasendi M. Saldua
Date: December 12, 2022

In 1949, Dr. Rudolf Flesch published The Art of Readable Writing, in which he proposed
a measure of text readability known as the Flesch Index. This index is based on
the average number of syllables per word and the average number of words per sentence
in a piece of text. Index scores usually range from 0 to 100, and they indicate
readable prose for the following grade levels:

Flesch Index -> Grade Level of Readability
0–30         -> College
50–60        -> High School
90–100       -> Fourth Grade

In this case study, we develop a program that computes the Flesch Index for
a text file.

For the purpose of the program, the following are defined accordingly:
Word - Any sequence of non-whitespace characters.
Sentence - Any sequence of words ending in a period, question mark, exclamation point,
colon, or semicolon.
Syllable - Any word of three characters or less; or any vowel (a, e, i, o, u) or pair of
consecutive vowels, except for a final -es, -ed, or -e that is not -le.

"""


# Introduce the program
print("This program determines the readability of a text using the Flesch Index.")

# Get user input
file = input("Please enter file name to test: ")

# Perform task
try:
    fhand = open(file, 'r')
    string_equiv = fhand.read()

    # Count the number of sentences
    sentence_count = 0
    punc_marks = ['.', '?', '!', ';', ':']
    for mark in punc_marks:
        sentence_count += string_equiv.count(mark)

    # Count the number of words
    words = string_equiv.split()
    word_count = len(words)

    # Count the number of syllables
    syl_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    exempt = ['s', 'd']
    
    # Examine each word
    for word in words:
        
        # Initialize everything
        syllables = []
        word_len = len(word)
        i = 0

        # Loop through each character
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
                    # Ellipsis (...) is counted as 3 syllables 
                    if (char == '.') and (word[i + 1] == '.'):
                        if word[i + 2] == '.':
                            for i in range(3):
                                syllables.append(char)
                            i += 3
                        else:
                            i += 2
                    i += 1
        syl_count += len(syllables)

    # Get the Flesch Index
    f = 206.835 - 1.015 * (word_count / sentence_count) - 84.6 * (syl_count / word_count)

    #Get the Grade Level Equivalent
    g = round(0.39 * (word_count / sentence_count) + 11.8 * (syl_count / word_count) - 15.59)
        

    print("\nFile name: %s" % file)
    print("Sentence count: %d" % sentence_count)
    print("Word count: %d" % word_count)
    print("Syllable count: %d" % syl_count)
    print("Flesch index: %.2f" % f)
    print("Grade Level Equivalent: %d\n" % g)

except:
    print("The file does not exist. Please try again.\n")
    






    
