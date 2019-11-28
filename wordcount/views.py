from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(requests):
    return render(requests,'home.html')

def about(requests):
    return render(requests,'about.html')

def count(requests):
    fulltext= requests.GET['fulltext']




    wordlist=fulltext.split()

    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            #increment
            worddictionary[word]+=1
        else:
            #add to worddictionary
            worddictionary[word]=1
    sortedwords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(requests,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})
