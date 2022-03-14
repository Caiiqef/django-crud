from django.contrib import admin  
from django.urls import path  
from user import views

urlpatterns = [  
    # path('', views.show),
    path('admin/', admin.site.urls),  
    path('usr', views.usr),  
    path('show',views.show),  
    # path('edit/<int:user_id>', views.edit),  
    path('update/<int:user_id>', views.update),  
    path('delete/<int:user_id>', views.destroy),  
]  