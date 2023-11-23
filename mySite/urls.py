from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webapp/', include('webapp.urls')),
    path('', lambda request: redirect('user_auth:login'), name='index'),  # Redirect to login page in user_auth app
    path('blog/', include('blog.urls')),
    path('polls/', include('polls.urls')),
    path('user_auth/', include("django.contrib.auth.urls")),
    path('user_auth/', include("user_auth.urls")),
]
