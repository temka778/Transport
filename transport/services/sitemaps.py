from django.contrib.sitemaps import Sitemap
from .models import Technique

class TechniqueSitemap(Sitemap):
    changefreq = "hourly"
    priority = 1.0

    def items(self):
        return Technique.objects.all()