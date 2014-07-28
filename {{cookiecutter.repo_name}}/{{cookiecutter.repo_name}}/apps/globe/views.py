from django.shortcuts import render


def under_construction(request):
    return render(request, 'globe/under_construction.html')
