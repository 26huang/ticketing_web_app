from django.http import HttpResponse
from django.shortcuts import render
from ticketing.models import Ticket
import random
import string


def random_string(string_length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def index(request):
    # return HttpResponse("Hello World!")
    return render(request, 'index.html')


def submit(request):
    # new_ticket = Ticket(submitter=random_string(), body='Need support with a bug.')
    # new_ticket.save()

    if request.method == 'POST':
        username = request.POST.get('username')
        body = request.POST.get('body')
        new_ticket = Ticket(submitter=username, body=body)
        new_ticket.save()
        return HttpResponse("successfully submitted ticket!")
    return render(request, 'submit.html')


def tickets(request):
    all_tickets = Ticket.objects.all()

    return render(request, 'tickets.html', {'tickets': all_tickets})