from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.getdata),

   path('getstid/<int:id>/', views.getstid),
   path('insert/', views.insert),
   path('update/<int:id>', views.update),
   path('deleteid/<int:id>', views.deleteid),
   path('commentdata/<int:post_id>/', views.commentdata),
   #path('post/<int:post_id>/comments/',commentdata, name='commentdata'),
  
]