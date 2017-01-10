"""sesdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from searchImage import views as cmviews
from django.views.static import serve
import settings

uploaded_dir = settings.UPLOADED_PATH

urlpatterns = [
    url(r'^upload/', cmviews.upload),
    url(r'^search/', cmviews.upload),
    url(r'^admin/', admin.site.urls),
    url(r'^index/', cmviews.homepage),
    url(r'^upload_search/', cmviews.upload_search),
    url(r'^images/(?P<path>.*)', serve, {'document_root': '/home/jimmy/bkmeans_imagenet'}),
    url(r'^uploaded/(?P<path>.*)', serve, {'document_root': uploaded_dir}),
]
