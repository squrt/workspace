from django.contrib.sitemaps import Sitemap
from Test.models import Book


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Book.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
