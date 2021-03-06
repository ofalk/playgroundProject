"""playground_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import homePg.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePg.views.home, name='home'),
    path('impressum', homePg.views.impressum, name='impressum'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

def javascript_settings():
    js_conf = {
        'page_title': 'Home',
    }
    return js_conf
