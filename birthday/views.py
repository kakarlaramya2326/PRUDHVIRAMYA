from django.shortcuts import render


def home(request):
    return render(request, 'birthday/home.html')

def story(request):
    return render(request, 'birthday/story.html')

def memories(request):
    return render(request, 'birthday/memories.html')

def reasons(request):
    return render(request, 'birthday/reasons.html')
def birthday(request):
    return render(request, 'birthday/birthday.html')