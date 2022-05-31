import re
from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'website/main_page.html', {})

def socialMedia(request):
    return render(request, 'website/socialMedia_page.html', {})