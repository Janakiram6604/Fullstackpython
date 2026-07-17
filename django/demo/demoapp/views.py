from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import ReservationForm


def hello_world(request):
    return HttpResponse("hello word")


class helloindia(View):
    def get(self, request):
        form = ReservationForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("success")
        return render(request, 'index.html', {'form': form})
