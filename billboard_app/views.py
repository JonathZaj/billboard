from django.shortcuts import render
from .models import Billboard


def index(request):
    context = {"billboard": Billboard.objects.all()}
    return render(request, 'Billboard_app/index.html', context)

