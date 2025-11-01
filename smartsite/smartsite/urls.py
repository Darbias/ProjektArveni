from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# ✅ për sitemap
from django.contrib.sitemaps.views import sitemap
from pages.sitemaps import StaticViewSitemap, ProjectSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "projects": ProjectSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),  # faqet kryesore
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]

# ✅ për media files në zhvillim (foto, logo, cover)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
