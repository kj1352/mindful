from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^offerings$', views.offerings, name="offerings"),
    url(r'^about-us$', views.aboutus, name="aboutus"),
    url(r'^blog$', views.blog, name="blog")
]
