from django.shortcuts import render


def index(request):
    context = {
        'mes': 'My new message',
        'mes2': 'My second new message'
    }
    return render(request, 'posts/index.html', context)
