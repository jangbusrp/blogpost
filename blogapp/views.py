from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser, CreatePosts, CommentAdds
from .models import CreatePost, CommentsAdd
from django.contrib.auth.models import User
from django.contrib import messages 

from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    return render(request, 'base.html')


def registeruser(request):
    form = CreateUser()
    if request.method =='POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Created Account")  
            return redirect('login')

    context = {'form':form}
    return render(request, 'register.html', context)    

def loginuser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password = password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('/home')
                
    context ={}
    return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/home')
    
    return HttpResponse('loginuser')

def createpost(request):
    form =CreatePosts()
    if request.method == 'POST':
        form = CreatePosts(request.POST, request.FILES )
        if form.is_valid():
            form.save()
            messages.success(request, "Create post Successfully ")
            return redirect('/home')
    context = {'form':form}
    return render(request, 'createpost.html', context) 

            # Get the current instance object to display in the template
    #         posts = form.instance
    #         return render(request, 'home.html', {'form': form, 'posts': posts})
    # else:
    #     form = CreatePost()
    # return render(request, 'createpost.html', {'form': form})

    
    # form =CreatePost()
    # if request.method =='POST':
    #     form = CreatePost(request.POST)
    #     if form.is_valid():
    #         form.save() 
    #         return redirect('/home')
    # context = {'form':form

    
    # }
    # return render(request, 'createpost.html', context)




def home(request):
    
    post= CreatePost.objects.all().order_by('-create_date')
    # comment= CommentsAdd.objects.filter(post=post)
    
    context = {

        'post':post

    }
    return render(request , 'home.html', context)



def detailspost(request):
    posts= CreatePost.objects.filter(post_user=request.user).order_by('-create_date')
    context = {

        'posts':posts

    }
    return render(request , 'details.html', context)




def userpost(request):
    posts= CreatePost.objects.filter(post_user=request.user).order_by('-create_date')
    context = {

        'posts':posts

    }
    return render(request , 'userpost.html', context)




def editpost(request, pk):
    # posts= CreatePosts.objects.get(id=pk)
    # form =CreatePost(instance=posts)
    # if request.method =='POST':
    #     form = CreatePost(request.POST, instance=posts)
    #     if form.is_valid():
    #         form.save() 
    #         return redirect('/details')
    # context = {'form':form}
    # return render(request, 'edit.html', context)

    posts= CreatePost.objects.get(pk=pk)
    form =CreatePosts(instance=posts)
    if request.method == 'POST':
        form = CreatePosts(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            messages.success(request, "Edit Successfully")
            return redirect('/details')
    context = {'form':form}
    return render(request, 'edit.html', context) 




def deletepost(request, pk):
    posts= CreatePost.objects.get(pk=pk)
    if request.method== "POST":
        posts.delete()
        return redirect('/details')
    context = {'item': posts}
    return render(request, 'delete.html', context)



def addcomment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= CreatePost.objects.get(sno=postSno)
        comment=CommentsAdd(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
        
        
    return redirect("/home") 



