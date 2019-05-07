from django.shortcuts import render

def predict(request):
    context = {}
    Sentiment = request.POST.get('txt', None)
    return render(request, 'index.html', context)
