from django.conf.urls import url

from fields import views

urlpatterns = [
    url('^status/', views.status)
]
