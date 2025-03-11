from django.shortcuts import render, HttpResponse

def blog_list(request):
    return HttpResponse("You are at Blog Lists")

def blog_article(request):
    return HttpResponse("You are at Blog Article")

