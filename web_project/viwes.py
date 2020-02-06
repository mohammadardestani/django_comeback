
from django.http import HttpResponse
from django.shortcuts import render 


def home_page(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']
    word_count=fulltext.split()
    return render(request, 'count.html',{'user_text':fulltext, 'count':len(word_count)})    

def about(request):
    return render(request,'about.html')