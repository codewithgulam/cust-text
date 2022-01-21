# Coded by Rabs
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # getting Text
    djtext = request.POST.get('text', 'default')
    # checking checkbox on or off
    removepunc = request.POST.get('removepunc', 'off')
    upper_case = request.POST.get('upper_case', 'off')
    newline_remover = request.POST.get('newline_remover', 'off')
    extraSpace_remover = request.POST.get('extraSpace_remover', 'off')
    wordCount = request.POST.get('wordCount', 'off')
    analyzer = ""
    punctuations = '''!()-[]{};:'=+-,<>./?@#$%^&*"_~'''
    if removepunc == 'on':
        for char in djtext:
            if char not in punctuations:
                analyzer = analyzer + char
        param = {'analyzed_text': analyzer, 'purpose': 'Removing Punctuation'}
        djtext = analyzer
        # return render(request, 'analyzed.html', param)

    if(upper_case == 'on'):
        analyzer = ""
        for char in djtext:
            analyzer = analyzer + char.upper()
        param = {'analyzed_text': analyzer, 'purpose': 'Capitilize Text'}
        # return render(request, 'analyzed.html', param)
        djtext = analyzer

    if(newline_remover == 'on'):
        analyzer = ""
        for char in djtext:
            if(char != "\n" and char != '\r'):
                analyzer = analyzer + char
        param = {'analyzed_text': analyzer, 'purpose': 'Removing Newlines'}
        # return render(request, 'analyzed.html', param)
        djtext = analyzer

    if(extraSpace_remover == 'on'):
        analyzer = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzer = analyzer + char
        param = {'analyzed_text': analyzer, 'purpose': 'Removing Extra Space'}
        # return render(request, 'analyzed.html', param)
        djtext = analyzer

    # if(wordCount == "on"):
    #     txt = "Word count is equals to"
    #     analyzer = len(djtext)
    #     param = {'analyzed_text': {txt, analyzer}, 'purpose': 'Counting words'}
    #     return render(request, 'analyzed.html', param)

    if (extraSpace_remover != 'on' and newline_remover != 'on' and upper_case != 'on' and removepunc != 'on'):
        return render(request, 'error.html')
        

    return render(request, 'analyzed.html', param)