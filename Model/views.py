from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def index(request):
    if request.method == "POST":
        Sentiment = request.POST['txt']
        print(Sentiment)
    

    return render(request, 'index.html', {'getvalue': Sentiment})