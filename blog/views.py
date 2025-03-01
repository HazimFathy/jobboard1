from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView , DeleteView , UpdateView ,CreateView , DetailView
from .models import Blog ,Comment , Category
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import CommentForm , BlogForm

# Create your views here.from django.shortcuts import render




class bloglist(ListView):
    model = Blog
    template_name = "blog_list.html"
    ordering= ['-create_at']
    paginate_by = 4
    queryset = Blog.objects.filter(active=True)
    



    
    
    
#add job def






def blog_detail(request, id):
    blog_detail = get_object_or_404(Blog, id=id)
    comments = Comment.objects.filter(post=blog_detail)  # تصحيح الحقل إلى post
    blog_list = Blog.objects.all()
    category_list = Category.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.post = blog_detail  # تصحيح الحقل إلى post
            myform.owner = request.user
            myform.save()
            return redirect(reverse('blogs:blogdetail', args=[id]))  # تصحيح اسم الصفحة
    
    else:
        form = CommentForm()

    context = {
        'blog': blog_detail,
        'form': form,
        'comments': comments,
        'blog_list': blog_list,
        'category_list': category_list
    }
    
    return render(request, 'blog/blog_detail.html', context)






@login_required  
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(user=request.user)  
            return redirect(reverse('blogs:blog')) 
    else:
        form = BlogForm()

    return render(request, 'blog/add_blog.html', {'form': form})
