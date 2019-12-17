from django.shortcuts import render
from django.http import HttpResponse
from .about import Info, SnippetForm
from django.contrib import messages
from django.http import JsonResponse

# def index(request):
#     data = Info
#     return render(request, "index.html",
#                 {"datafrom django.contrib import messages": data})

def snippet_details(request):
    if request.method == 'POST':
        data = SnippetForm(request.POST)
        if data.is_valid():
            data.save()
            messages.success(request, 'Your record has been submit successfully!')  # <-
            #messages.success(request, 'Your record has been submit successfully!', extra_tags='alert')
    data = SnippetForm()
    return render(request, "index.html", {"data": data})


def index(request):


    if request.method == 'POST' :
        data = Info(request.POST)
        if data.is_valid():
            name = data.cleaned_data['name']
            email = data.cleaned_data['email']
            description = data.cleaned_data['description']
            image_url = data.cleaned_data['image_url']
            print(name, email, description, image_url)


    data = Info()
    return render(request, "index.html", {"data": data})


# def snippet_details(request):
#     if request.method == 'POST':
#         data = SnippetForm(request.POST)
#         if data.is_valid():
#             data.save()
#
#     data = SnippetForm()
#     return render(request, "index.html", {"data": data})

