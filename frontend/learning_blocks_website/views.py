from django.shortcuts import render


def home(request):
    return render(request, 'learning_blocks_website/home.html')
