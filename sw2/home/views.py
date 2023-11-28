from django.shortcuts import render
from home.models import books
from django.views.generic import ListView,DetailView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView,DeleteView
from django.contrib.auth.models import User


# Create your views here.
class bookslistview(ListView):
    model = books
    template_name = 'home/books.html'
    context_object_name = 'book'

class registration(CreateView):
    form_class=UserCreationForm
    template_name='registration/register.html'
    success_url='/acc/login'


def search(request):
    if 'search' in request.POST:
        query=request.POST['search']
        name=User.objects.get(id=query)
        return render(request,'home/specuser.html',context={'name':name})

class users(ListView):
    model = User
    template_name = 'home/users.html'
    context_object_name = 'user'

class booksDetailview(DetailView):
    model = books
    template_name = 'home/show.html'   

class DeletebookView(DeleteView):
    model = books
    template_name = 'home/delete.html'
    success_url = '/home'
