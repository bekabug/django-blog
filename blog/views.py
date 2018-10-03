from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
        posts = Post.objects.order_by('-created_date')
        return render(request, 'blog/post_list.html', {'posts': posts})

def style_guide(request):

        # Render the HTML template index.html with the data in the context variable
        return render(request, 'blog/style_guide.html', context=context)