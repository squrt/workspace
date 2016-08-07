"""workspace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps import Sitemap, GenericSitemap
from Test.models import Entry
from Test.blogsitemap import BlogSitemap

admin.autodiscover()

info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}
sitemaps = {
    # 'flatpages': FlatPageSitemap,
    'Test': GenericSitemap(info_dict, priority=0.6),
    # 'blogsitemap':BlogSitemap,
}


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Test/index/(?P<id>\d{1})/$', 'Test.views.index', {}),
    url(r'^Test/employee/$', 'Test.views.index4'),
    url(r'^Test/author/$', 'Test.views.show_author'),
    url(r'^Test/book/$', 'Test.views.show_book'),
    url(r'^Test/register/$', 'Test.views.register'),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^Test/pachong/$', 'Test.pachong.pachong'),
    url(r'^Test/xml/dom$', 'Test.foundation.dom'),
]

'''
urlpatterns += ['Test.views',
    url(r'^Test/index/1', 'index1'),
    url(r'^Test/index/2', 'index2'),
    url(r'^Test/index/3', 'index3'),
]'''
