from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Ticket

class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = '__all__'
    success_url = reverse_lazy('blog:home')

# Create your views here.
@login_required
def home(request):
    return render(request, 'blog/home.html')
