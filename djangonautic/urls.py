
from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^articles/',include('articles.urls')),
    url('^about/$',views.about),
    url('^$',views.homepage)
]

urlpatterns+=staticfiles_urlpatterns()
