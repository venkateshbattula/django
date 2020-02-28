from django.shortcuts import render
from django.http import HttpResponse
from .models import users
# Create your views here.
from django.template import loader


def index(request):
    all_users = users.objects.all()
    html = ''
    for i in all_users:
        url = '/register/' + str(i.id) + '/'
        html += '<a href="' + url + '">' + str(i.name) + '</a><br>'
    return HttpResponse(html)


def details(request, user_id):
    return HttpResponse("<h2>This is the page of the user_id:" + str(user_id) + "</h2>")
