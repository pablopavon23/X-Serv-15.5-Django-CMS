from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms import views

urlpatterns = patterns('',
    url(r'^$', views.barra, name='barra'),
    url(r'^pagina/(\d+)$', views.pagina, name='bebida'),
    url(r'^admin/', include(admin.site.urls)),
)
