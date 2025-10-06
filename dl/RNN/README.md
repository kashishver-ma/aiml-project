# recurrent neural network

how gpt ans us ?

like what is python?

1.tokenisation of words
2.parts of speech classify

'what'-went to model
come back to take 'is'
then is nd then python

convert to vector using nlp

pass this vector to model !!

Type of RNN :

4 main

1. one to one

signle input single output
use case :

2. one to many

single input multiple output
use case: list down to gpt

3. many to one

more input nd one output
use case : true false y/n

4. many to many

many input , multiple output

GRY and lstm (Adv version of RNN)

LSTM : long short test memory
draw back of RNN - prev data is not in memory
solve vanishing gradient problem

Architecture :

input gate - input
forget gate - remove prev data
outpute gate - produce output

one more

GRU : gather recurrent neural unit
more adv version

2 gate :
update gate (add /remove) and Reset (memory reset) gate

diff btwn lstm and gru:

architecture difference

use case:

lanuguage transfer
speech recognisation

memo link have notes

NLP:

1. LOWERCASE lower function
2. remove html tag regular expressions
3. remove url nlp
4. chatword emoji removal
5. spelling correction
6.

advance : pos tagging

text vectorisation :
word to number conversion

1. bag of word
   label encoding
   custom feature
   tfidf
   n-grams
   ohe

bag of words:

i love dog
i love cat

bag= i love dog cat (4)

vector=[1,1,1,0]
v2=[1,1,0,1]

adv:
simple easy

dis: out of vac

this is gd movie ,
this is nt a gd movie

2. N grams:
   uni gram , bi gram , tri..

tokenisation
disad: out of vocu
dimension increase acc dec

3. TF-IDF:

term freq inverse document freq

find unique
find tf table
idf cl

res=tf\*idf

custom features: research ongoing
