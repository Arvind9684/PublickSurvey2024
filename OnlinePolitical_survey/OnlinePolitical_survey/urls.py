"""
URL configuration for OnlinePolitical_survey project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from public import views
from public.views import reg_mobile,votting

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('change_language/<int:option_id>',views.change_language,name='change_language'),
    path('reg_mobile',views.reg_mobile,name='reg_mobile'),
    path('logout',views.logout,name='logout'),
    path('insertchat',views.insertchat,name='insertchat'),
    path('votting/',views.votting,name='votting'),
    path('show_result',views.show_result,name='show_result'),
]
