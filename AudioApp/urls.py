from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', views.upload_audio, name='upload_audio'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('audio/<slug:slug>/', views.serve_audio, name='serve_audio'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    