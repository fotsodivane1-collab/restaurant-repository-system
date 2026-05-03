from django.shortcuts import render

def reserve(request):
    return render(request, 'reserve/reserve.html', {})