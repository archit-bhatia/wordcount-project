from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html',{'name':'archit'})

def about(request):
    return render(request,'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordmap = {}
    for word in wordlist:
        if word in wordmap:
            wordmap[word] +=1
        else:
            wordmap[word] = 1

    sortedlist=sorted(wordmap.items(),key=operator.itemgetter(1),reverse =True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'wordlist':sortedlist})

def boot(request):
    return render(request,'boots.html')


def homes(request):
    return HttpResponse('<h1>Jai Shri Ram</h1>')


def name(request):
    return HttpResponse('<h3><i>archit bhatia</i></h3>')
