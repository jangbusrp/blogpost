from django.urls import path
from blogapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('addcomment', views.addcomment, name="addcomment"),
    path('index/',views.index, name='index' ),
    path('register/', views.registeruser, name= 'register'),
    path('login/', views.loginuser, name="login"),
    path('logout/', views.logoutuser, name="logout"),
    path('post/', views.createpost, name="createpost"),
    path('', views.home, name="home"),
    
    path('details/', views.detailspost, name="details"),
    path('edit/<str:pk>/', views.editpost, name="edit"),
    path('delete/<str:pk>/', views.deletepost, name="delete"),
    path('userpost/', views.userpost, name="userpost"),

    # path('addcomment/<str:pk>/', views.addcomment, name="addcomment"),



]