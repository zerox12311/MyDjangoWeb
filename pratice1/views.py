from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostModelForm


from .models import Post
# Create your views here.

def Index(request):
    posts = Post.objects.all()
    return render(request,'posts/index.html',{'posts':posts})

def New(request):
    # if request.method == 'POST':
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     if title == '' or content == '':
    #         return render(request,'posts/new.html',{
    #             'error':['有欄位沒寫']
    #         })

           
    #     Post.objects.create(title=title,content=content)
    #     return redirect('posts')
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('posts:')
    return render(request,'posts/new.html',{
        'form':form
    })

def edit(request, pk):
    post = get_object_or_404(Post,pk=pk)
    form = PostModelForm(request.POST or None,instance=post)
    if form.is_valid():
        form.save()
        return redirect('posts:')
    return render(request,'posts/edit.html',{
        'form':form
    })

def delete(request, pk):
    post = get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('posts:')

def show(request, pk):
    # post = Post.objects.get(pk = pk)
    post = get_object_or_404(Post,pk=pk)
    return render(request,'posts/show.html',{'post':post})