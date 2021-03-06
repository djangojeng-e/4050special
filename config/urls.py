"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from apply.views import login_view, logout_view
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apply.urls')),
    path('login/', login_view, name='login_page'),
    path('logout/', logout_view, name='logout_page'),
    path('community/', include('community.urls')),
    path('resources/', include('resources.urls')),
]

# urlpatterns += static(
#     prefix=settings.MEDIA_URL, 
#     document_root = settings.MEDIA_ROOT,
# )



if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(prefix= settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    print(settings.MEDIA_URL)
    print(settings.MEDIA_ROOT)
    print(debug_toolbar.urls)
    