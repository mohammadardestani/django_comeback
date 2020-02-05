
from django.http import HttpResponse


def home_page(request):
    return HttpResponse(content="this is home page")
    