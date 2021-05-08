
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    writtentext = request.GET['fulltext']
    wordlist = writtentext.split()

    worddict = {}

    for word in wordlist:
        if word in worddict:
            #Increase
            worddict[word] += 1
        else:
            #add to the dictionary
            worddict[word] = 1
#this part sort the words from the most common to the less one
    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'fulltext':writtentext, 'number':len(wordlist), 'sortedwords':sortedwords})

#def cars(request):
    #return HttpResponse('<h1>Teslas are cool!</h1>')
