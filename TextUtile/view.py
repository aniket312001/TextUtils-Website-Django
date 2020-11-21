
from django.http import HttpResponse
from django.shortcuts import render
import string

def index(request):
    return render(request,'index.html')


def data(request):

    text = request.POST.get('txt')
    
    new = text
    if request.POST.get('removepunc') == 'on':
        new = [char for char in new if char not in string.punctuation]
        new = ''.join(new)
    
    if request.POST.get('upper') == 'on':
        new = new.upper()

    if request.POST.get('removespace') == 'on':
        new = [char for char in new if char!=' ']
        new = ''.join(new)

    param = {"mytext":text,'punc':new}

    return render(request,'data.html',param)
