# Language Exceptions

## Detect multi-languages:

### Problem:
What approach would you use to automatically determine what languages are used in a given message? Please keep in mind that messages do not always contain two different languages, they can also contain just one language. If you believe that some situations cannot be handled by your implementation, please specify which ones and why.

### Proposed Solution:
The first idea was to tokenize the entire message into words and check the language for each word. But this method showed poor results as two different languages may share similar words.

Instead, I used N-grams (a sequence of successive N words) to detect the existent languages in the user's message. N-grams are used for a variety of things: auto completion of sentences, auto spell check... Here, I would like to check if using N-grams for languages detection (in a multilingual environment) would give good results.

I started by generating all the N-grams (where N is a parameter to be optimized: 3-gram for example) for a given message. Then, I used langdetect, a pre-built package for automatic language detection applied to each N-gram sequence separately. The good thing about langdetect, is that it is well optimized and that it supports 55 languages including French, English, Arabic, Chinese ...
I then calculated the frequency of each detected language. If the first most frequent language is predominant (with a frequency of 0.80), I only output this language. If not, I extract the top max_lang most frequent (Where max_lang is a user parameter: top 2 for example)

The solution is then tested using different messages with multiple languages.

The remark is that the solution is sensitive to the choice of words_to_combine, max_lang. So those parameters need to be tuned correctly. Adding to that, the Language detection algorithm is non-deterministic, which means that if you try to run it on a text which is either too short or too ambiguous, you might get different results every time you run it.

Further improvement could be by training your own Neural Network language detection model.

## Detect word variation

### Problem:
How would you proceed to detect if a given word is a variation of the word “blackhat”? Please write a Python function that determines if a string is a variation of this word. How would you generalize this to any given term?

### Proposed Solution:
Based on the given example: blackkkhat, bl@khat, b__la-c_k_hat are variations of the word blackhat. Those variations include non alpha characters and duplicated ones, also the @ symbol was alternated with the a character.

So the idea is to create a function that:

Replaces the "@" with "a"
Removes the duplicates
Removes all non alpha characters
A generalisation on this would be by:

Removes the duplicates
Removes all non alpha characters
Creating a dictionary of the possible character to be alternated with other ones.
Have a look at the python implementation below!
