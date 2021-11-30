from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    try:
        age_b = request.GET.get('lname', 2078)
        age_c = int(age_b)
        age_ur = 2078-age_c
        return render(request, "school\home.html", {'age_ur': age_ur})
    except:
        return HttpResponse("<h1>Please enter valid date of birth !")
