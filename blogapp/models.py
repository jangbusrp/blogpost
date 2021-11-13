from django.db import models

# Create your models here.
from django.contrib.auth.models import User

#Create your models here.
class CreatePost(models.Model):
    sno= models.AutoField(primary_key=True)
    caption = models.CharField(max_length=255, null = True)
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.TextField(null= True, blank=True)
    image = models.ImageField(upload_to = "images", null= True, blank=True )
    create_date = models.DateTimeField(auto_now= True)
    edit_date = models.DateTimeField(auto_now= True)
    hide_show = models.BooleanField(default=False)


    def __str__(self):
        return self.caption


class CommentsAdd(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(CreatePost, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username

   


  