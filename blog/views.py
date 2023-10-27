from django.shortcuts import render
from django.views.generic.base import View
from .forms import PostCreateForm
# Create your views here.
class BloglistView(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'blog_list.html', context)

class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form=PostCreateForm()
        context={
            'form':form
        }
        return render (request,'blog_create.html', context)
    
    def post(self, request, *args, **kwargs):
        context={
        }
        return render (request,'blog_create.html', context)