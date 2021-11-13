from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import datetime
from .models import CreatePost,CommentsAdd



class CreateUser(UserCreationForm):
    class Meta:
        model= User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1','password2']




# class CreatePost(CreateUser):
#     caption = forms.CharField()
#     post_text = forms.CharField()
#     image = forms.ImageField()
#     create_date = forms.DateField(initial=datetime.date.today)
#     edit_date = forms.DateTimeField(initial=datetime.date.today)

    # caption = models.CharField(max_length=255, null = True)
    # post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # post_text = models.TextField(null= True, blank=True)
    # image = models.ImageField(upload_to = "images", null= True, blank=True )
    # create_date = models.DateTimeField(auto_now= True)
    # edit_date = models.DateTimeField(auto_now= True)



class CreatePosts(ModelForm):
    class Meta:
        model = CreatePost
        fields =('sno','caption','post_user','post_text','hide_show', 'image')
        



class CommentAdds(ModelForm):
    class Meta:
        model = CommentsAdd
        fields =('sno','comment','user','post')