from django.shortcuts import render
from .models import About


# Create your views here.
def main(request):
    return HttpResponse('ok')


def about(request):
    about = About.objects.all()

    context = {
        'about': about,
    }
    return render(request, 'pages/about.html', context)



def contact(request):
    return render(request, 'pages/contact.html')
