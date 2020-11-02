import bs4
import requests
import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import string
import re
import operator

def bigram(doc):
    
    result = []                                    #list for the result
    
    for word in range(len(doc) - 1):               # parse through the sentence add two words
        first_word = doc[word]
        second_word = doc[word + 1]
        element = (first_word, second_word)
        result.append(element)
    return result

d = {}
def find_freq_uni(unigram):                         # scan through the unigram
    for text in unigram:                            # return text,count in dict format
        if text not in d:
            d[text] = 1
        else:
            d[text] +=1
    return d


f = {}
def find_freq_bi(bigram):                           # scan through the unigram                
    for text in bigram:                             # return text,count in dict format                           
        f[text] = bigram.count(text)
    return f


def sort_dict(d):                                   # sort the list based on values(int)
    L = sorted(d, key=lambda i: int(d[i],))
    return L


def uni_bi_values(url):   


    try:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text,'lxml')
    except:
        return ['N/A'],['N/A']

    for script in soup(["script", "style"]):
        script.extract()                               # rip it out]
    
    text = soup.get_text()
    
    
    lines = (line.strip() for line in text.splitlines()) # remove leading and trailing space 


   
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))  # break multi-headlines into a line each


    
    text = '\n'.join(chunk for chunk in chunks if chunk)    # drop blank lines

    

    punct_removed_text = re.sub(r'[^\w\s]', '',text)        #removes punctuation
    text_tokens = word_tokenize(punct_removed_text)         #make in token format
    unigram_result = [word for word in text_tokens if not word in stopwords.words()]   #eliminating stop words
    
    unigram_dict = find_freq_uni(unigram_result)
    sorted_unigram = sort_dict(unigram_dict)
    bigram_result = bigram(unigram_result)
    bigram_dict = find_freq_bi(bigram_result)
    sorted_bigram = sort_dict(bigram_dict)
    
    return sorted_unigram[-1:-20:-1],sorted_bigram[-1:-20:-1]        # returning top 20 values

#a,b = uni_bi_values('https://www.linkedin.com/feed/hashtag/?keywords=%23ScholarlyPublishing')

#print(a)
#print(b)