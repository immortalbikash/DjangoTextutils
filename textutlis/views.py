# I have created this website - Bikash
#15

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params = {'name': 'Bikash', 'place': 'Gaighat'}
    return render(request, 'index.html')
    # return HttpResponse('''<h1>Hello world</h1> <a href= "https://www.google.com/">Google</a>''')

# def about(request):
#     return HttpResponse('''About <a href="http://127.0.0.1:8000">Back</a>''')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'false')
    fullcaps = request.POST.get('fullcaps', 'false')
    newlineremover = request.POST.get('newlineremover', 'false')
    extraspaceremover = request.POST.get('extraspaceremover', 'false')
    wordcount = request.POST.get('wordcount', 'false')
    # print(removepunc)
    # print(djtext)

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        
        params = {'purpose': 'Remove punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Upper case', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        djtext = analyzed
            # return render(request, 'analyze.html', params)

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if wordcount == "on":
        length_word = len(djtext)

        params = {'purpose': 'Word Counting', 'analyzed_text': 'The length of word is '+str(length_word)}
        djtext = length_word
    return render(request, 'analyze.html', params)

    # if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and wordcount != "on"):
    #     return HttpResponse("Please select any operator")

def navigation(request):
    return HttpResponse('''<h1>Navigation</h1><br>
    <a href="https://www.google.com">Google</a><br>
    <a href="https://www.facebook.com">Facebook</a>''')





# def katwal(request):
#     return HttpResponse("This is katwal")

# def gaighat(request):
#     return HttpResponse("This is gaighat")

# def ashari(request):
#     return HttpResponse("This is ashari")
