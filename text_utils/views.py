# I have created this file -Shubham
from django.http import HttpResponse
from django.shortcuts import render
import os
def index(request):
    return render (request, 'index.html')


def analyze(request):
    # get the text
    djtext=request.POST.get ('text', 'default')

    # check checkbox value
    removepunc=request.POST.get ('removepunc', 'off')
    fullcaps=request.POST.get ('fullcapitalize', 'off')
    remover=request.POST.get ('line_Remover', 'off')
    space_Remover=request.POST.get ('space_Remover', 'off')
    char_count=request.POST.get ('char_count', 'off')
    f=0
    analyzed=""
    output=""

    # check with checkbox is on
    if removepunc == 'on':
        f+=1
        punctuations='''!()-[]{};:\'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed + char

        djtext=analyzed
        output+='Removed Punctuations  '
        params = {'purpose': output, 'analyzed_text': analyzed}

    # -------------------------------------------- UPPERCASE----------------------------------------------------------
    if fullcaps == 'on':
        f+=1
        analyzed=""
    for char in djtext:
        analyzed=analyzed + char.upper ()

    djtext=analyzed
    output+='Capitalize  '
    params={'purpose': output, 'analyzed_text': analyzed}


# ------------------------------------------------ NEW LINE REMOVER -----------------------------------------------------
    if remover == 'on':
        f+=1
        analyzed=""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed=analyzed + char

        djtext=analyzed
        output+='new line removed'
        params={'purpose': output, 'analyzed_text': analyzed}

    # ------------------------------------------------  SPACE REMOVER  --------------------------
    if space_Remover == 'on':
        f+=1
        analyzed=""
        #print(analyzed)
        for index, char in enumerate (djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed=analyzed + char

        djtext=analyzed
        output+="Space Removed"
        params={'purpose': output, 'analyzed_text': analyzed}

    # ------------------------------------------------  CHAR COUNT  --------------------------
    if char_count == 'on':
        f+=1
        char_count_dict={}
       # analyzed=""

        for i in djtext:
            if i in char_count_dict:
                char_count_dict[i]+=1
            else:
                char_count_dict[i]=1

        # analyzed=str(char_count_dict);
        analyzed+="\n char count \n"
        for i in char_count_dict:
            analyzed+=i + "  " + str (char_count_dict[i]) + "\r\n"

        params={'purpose': 'char count', 'analyzed_text': analyzed}


    if (f > 0):
        return render (request, 'analyze.html', params)
    else:
        return HttpResponse ("Error")
