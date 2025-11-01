from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Project

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    def items(self):
        return ["home", "about", "services", "projects", "contact", "quote"]  # <-- about

    def location(self, item):
        return reverse(item)

class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7
    def items(self):
        return Project.objects.all()
    def location(self, obj):
        return reverse("project_detail", kwargs={"slug": obj.slug})
