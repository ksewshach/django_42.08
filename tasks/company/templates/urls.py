from django.contrib import admin
from django.urls import path
from company.views import main, contacts, about_company, management_company, news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main),
    path('contacts/', contacts),
    path('about_company/', about_company),
    path('management/', management_company),
    path('news/', news),
    
    
    
    
    
]