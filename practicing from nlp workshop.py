# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 09:03:30 2020

@author: tamanna
"""
#from week 7_list
some_text=['my', 'name', 'is', 'tm']
some_text[3]= 'secret'

for word in some_text:
    word=word.upper()
    print(word)
print(some_text)
 for i in range(len(some_text)):
     some_text[i]=some_text[i].upper()
     print(some_text[i])
 print(some_text)

text2= ['hey,', 'how', 'are', 'you?'] #assign a list to a variable
punc=[',', '!', '?', '.'] #make a list of relevant punctuation marks
for i in range(len(text2)): #iterate through every item in the list
    if text2[i][-1] in punc: #for every word, if the last element is punctuation
        text2[i]=text2[i][:-1]  #reassigning every item in the list uotp the last element
        
print(text2)
#noun phrase generator
determiner= ['a', 'an', 'the']
adjective = ['good', 'bad', 'ugly']
nouns= ['girl', 'boy']
for det in determiner:
    for adj in adjective:
        for noun in nouns:
            print(det, adj, noun)
#mantra
mantra= ['code', 'python']*3
mantra
    
mantra.index('python')
mantra.count('code')
#propoer noun generator
PN= ['Sam', 'Rob', 'adrian', 'john', 'Halsy'] #make a list

for i in range(len(PN)): #for every iytem in the list
    if PN[i][0].isupper(): #if the first element of every item is upper
        print(PN[i])
#sorted list
my_list=[1234, 'sam', 345, 'rob', 'john', 3]
emp_lis=[] #creating an empty list
emp_st=[] #creating an empty string
for i  in range(len(my_list)): #for every item in my list
    if  isinstance(my_list[i], int): #if the item is an integer
        emp_lis.append(my_list[i]) #append the item to the empty list
        emp_lis.sort() #sort the list 
    if isinstance(my_list[i], str): #if the item in the list is a string
        emp_st.append(my_list[i]) #append it to the empty string
        emp_st.sort() #sort the string
print(emp_lis)
print(emp_st)

#another alternative
my_list=[1234, 'sam', 345, 'rob', 'john', 3]
emp_lis=[] #creating an empty list
emp_st=[] #creating an empty string
for item in my_list: #for every item in my list
    if  isinstance(item, int): #if the item is an integer
        emp_lis.append(item) #append the item to the empty list
        emp_lis.sort() #sort the list 
    if isinstance(item, str): #if the item in the list is a string
        emp_st.append(item) #append it to the empty string
        emp_st.sort() #sort the string
print(emp_lis)
print(emp_st)

#from list chapter. produces four output though. maynot be the idea solution

def list_check(my_phrase, my_indi):
    my_phrase1=my_phrase.split()
    my_indi1=my_indi.split()
    for item in my_phrase1:
        if item in my_indi1:
            print('the item is in the list')
        else:
            print('the item is not there')
my_phrase=('I love my daughter')
my_indi=('I enjoy reading my books')

#an laternative
def verify(word1): #defining the function
    word1_lis=word1.split() #converting the given string into a list
    my_lis=['a', 'an', 'the'] #specifying a list of my choosing
    for i in range(len(my_lis)): #for every item in my chosen list
        if my_lis[i] in word1_lis: #if that item is in the first list
            print(my_lis[i] +  ' is in the list') #print that item is in the list
verify('I have the book')
#counting English articles, but not working properly
def coun_art(word2):
    word_lis=word2.split() #converting the string into a list
    Eng_art=['a', 'an', 'the'] #specifying the items to be counted 
    for item in Eng_art: #for each item in that list
        wordy=word_lis.count(item) #count that item in the given string
        print(wordy)
      
coun_art('I hate the book')
coun_art('The articles in English grammar are the and a an and in certain contexts some An and a are modern forms of the Old English an which in Anglian dialects was the number one')
     
#an alternative of the above code
def coun_art(word2):
    count=0 #specifying the base of count
    Art=['a', 'an', 'the'] #specifying the items to be searched
    word_lis=word2.split() #converting the string into a list
    for item in word_lis: #for each item in the list
        if item in Art: #if item in the article list
            count+=1  #count
    print(count)
            
     
coun_art('I hate the book')
coun_art('The articles in English grammar are the and a an and in certain contexts some An and a are modern forms of the Old English an which in Anglian dialects was the number one')
    
#from dictionery session# my solution,  IT WORKS!!!
def my_func(lis1): #defining the function
    for i in lis1: #for each element in the list
        if isinstance(i, str):  #if i is a string
            ver1=i.lower()    #i will be in lowercase, which is assigned to a variable
            print(ver1)   #print the variable
        if isinstance(i, list):  #if i is a list
            my_func(i)   #the program calls itself
text=['THANK you', ['NO comment', 'see you next time', 'happy to have helped'], ['please update MY information', 'ok'], 'Please']
my_func(text)
#another solution
def my_func(lis1): #defining the function
    for elem in lis1: #for each element in list 1
        if type(elem)==list:  #if type of the element is list
            my_func(elem)  #the function recurses
        else:      #otherwise
            print(elem.lower()) #elements are printed lowercase
mine=['THANK you', ['NO comment', 'see you next time', 'happy to have helped'], ['please update MY information', 'ok'], 'Please']
my_func(mine)   
#option 2
def help_desk(lis2):
    for element in lis2: #for every element in the list
        if lis2.count(element)==1:  #if number of element is 1
            elem1=element.split()   #make it a list
            print (len(elem1))     #print the length of the element
        else:                    #otherwise if the number fo elements is more than one, recurse the function
            help_desk(element)
tex=['THANK you', ['NO comment', 'see you next time', 'happy to have helped'], ['please update MY information', 'ok'], 'Please']
help_desk(tex)             
#cocreteness exercise
concreteness = {'red': 4.24, 'apple': 5, 'pear': 4.93, 'of': 1.67, 'there': 2.2}
items = ['apple', 'red', 'pear', 'a', 'funny', 'of', 'there']
for i in items:
    if i in concreteness:
        print('concreteness of ' + i + ' is: ', concreteness[i])
#concrteness2
items = ['apple','red','apple','red','red','pear']
my_dict=dict() #creating an empty dictionary
for item in items: #for every item in the list
    my_dict[item]=my_dict.get(item, 0)+1
print (my_dict)
#alice's adventures
text="""Alice was beginning to get very tired of sitting by her sister
on the bank, and of having nothing to do:  once or twice she had
peeped into the book her sister was reading, but it had no
pictures or conversations in it, `and what is the use of a book,'
thought Alice `without pictures or conversation?"""
def my_word (text):
    my_dict=dict()#creating a dictionary
    text1=text.split() #making the string into a list
    for item in text1: #for every item in the list
        my_dict[item]=my_dict.get(item, 0)+1 #attaching every item to the dictionary with their value
    print (my_dict)
my_word (text)        
    
#practice from week4
def num(a,b):
    if a < b or b==0: #specifying the conditions of impossibility
        print('it is impossible')
    else:
        for c in range (a+1): #otherwise for every number in the range from 0 to a
            if c%b==0: #if the number if divisible by b (with 0 as remainder)
                print(c)
num(6, 10)
num(20, 4)
        
#nltk
import nltk
from nltk import word_tokenize
from nltk.book import*
text1.count("give")
my_pers=text4.count("love")/len(text4)
pers=print(round(my_pers*100, 2), 'percent')

#processing my own texts on nltk
prose=open('F:\OneDriveGSU\OneDrive - Georgia State University\Python_practice\Julian.txt', 'r').read() #open and read the txt file
my_prose=word_tokenize(prose) #tokenize the open and read file
my_prose1=nltk.Text(my_prose) #convert the tokenized text into an nltk text
my_prose1.concordance("I") #start processign the text
dectic=['there', 'here', 'then', 'that'] #specified the things I want to find out
my_prose2=prose.split()#turning the text into a list
for word in my_prose2: #for every item in the list
    if word in dectic: #if it's in dectic
        myNum=my_prose2.count(word) #count their number and assign it to a variable
print(myNum) #print it

#from nltk: #doesn't  work
def word_vowels(words):
    words1=words.split()#turning the  input into a list
    count=0
    my_lis=['a', 'e', 'i', 'o', 'u']#specifying the list of vowels
    for word in words1:  #for each word in the list
        for i in my_lis: #for each item in the vowel list
            if i in word: #if the vowel in the word
                count+=1
                words2=words1.append(count).append(len(word))#appending the count of vowels and the length of word to the list and assigning that to a variable
    print(words2) #print the variable
words='I love you'
word_vowels(words)

#15_part1
def my_str(sent):
    sent1=sent.split()
    for item in sent1:
        sent2=sent1.count(item)
    print(sent2)
sent='I love you'
my_str(sent)
#part2 #does not work
def my_str(sent):
    sent1=sent.split() #turning the string to a list
    count=0 #base count is zero
    for i in sent1: #for each item in the list
        count+=i  #count frequency
    myline=sorted(i) #sort the words the assign those to a variable
    print(myline, count) #print sorted words and count
sent='I love her and love him'
my_str(sent)
 
#another solution of the above #does not work; had issues with sorting the dict
def my_sen(tence):
    sen1=tence.split() #turning the string to a list
    my_dic=dict()#specifying a dictioonary
    
    for item in sen1: #for each item in the list
        my_dic[item]=my_dic.get(item, 0)+1 #get the frequency of each item inthe list to a dictionary
    print (sorted(my_dic))
        
    
tence='I love her and love him'
my_sen(tence)

#revised code; this one works
def my_stg(sen):
    sen1=sen.split() #slpitting the input string and making it a list
    
    fdist=nltk.FreqDist(w.lower() for w in sen1) #make a frequency distribution of the lower case list
    for key in sorted (fdist.keys()): #for every key in the sorted dictionary keys
        print (key, fdist[key]) #print the keys and their frequency distributions
        
sen='I love you and love her and love them'
my_stg(sen) 

#repractice from wk 9
from nltk.probability import FreqDist
            
file_name=open('F:\OneDriveGSU\OneDrive - Georgia State University\Python_practice\hafsa.txt', 'r')
text=file_name.read() #read the opened file
text=text. strip().lower().split() #strip of white space, turn to lower case, and spllit into list
fdist1=FreqDist(text) #turn it into a dictionary
for item in fdist1.items():
    if item.startswith('a'):
        print (item, value)

        
##From nltk book_chapter#4#  1
lines=open('F:\OneDriveGSU\OneDrive - Georgia State University\Python_practice\Julian.txt', 'r')
def len_wor (lines):
    lines1=lines.read() #read the text file
    lines1=lines1.lower().split() #spliting the text into a list
    word=0 # specifying the baseline of word as 0
    total=0 #specifying the baseline of token as 0
    for token in lines1: #for every word int he list
        word+=1 #count the total number of words
        total += len(token) #count the total lengths of tokens
    print(total/word) #divide the length of tokens by the number of tokens and print it
len_wor(lines)   

##From nltk book_chapter#4# 2
def long_wor(tex):
    
    text1=tex.lower().split() #turning the text into a list
    longest= ' ' #defining an empty string
    for word in text1: #for every word in text
        if len(word)> len(longest): #if length of that word is greater than the empty string
            longest=word #word will be equal to the empty string
    print(longest) #print the longest word
tex='my name is julian and I am thirty seven years old'
long_wor(tex)
##From nltk book_chapter#4 #3 #the code worked but did not append anything
from nltk.util import ngrams
def nGram (sol):
    
    sol1=sol.lower().split() #turn the text into a list
    soln=[]    #create an empty list
    ngram1=list(ngrams(sol1, 2)) #create a list of ngrams)
    for i in range(len(ngram1)): #for every item in the ngram list
        if i==i+1: #if two successive items are the same
            soln.append(i) #append that item to the empty list
    print(soln) #print the list

sol= 'I want to want to love you'
nGram (sol)

##From nltk book_chapter#4 #3 #the code worked but did not append anything
from nltk.util import ngrams
def nGram (sol):
    sol1=sol.read()
    sol1=sol1.lower().split() #turn the text into a list
    soln=[]    #create an empty list
    ngram1=list(ngrams(sol1, 2)) #create a list of ngrams)
    for i in range(len(ngram1)): #for every item in the ngram list
        if i==i+1: #if two successive items are the same
            soln.append(i) #append that item to the empty list
    print(soln) #print the list

sol= 'I want to want to love you'
nGram (sol)
    

        
    
    


         
        
        
       
