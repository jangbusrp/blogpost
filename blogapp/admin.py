from django.contrib import admin
from .models import CreatePost, CommentsAdd
# Register your models here.


@admin.register(CreatePost)
class CreatePostAdmin(admin.ModelAdmin):
    list_display=("post_user","caption","post_text","create_date", "edit_date","hide_show", "image")



@admin.register(CommentsAdd)
class CommentAddAdmin(admin.ModelAdmin):
    list_display=("user",)