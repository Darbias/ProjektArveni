from django.urls import path, include
from . import views as v

urlpatterns = [
    # Faqja kryesore (Home)
    path("", v.home, name="home"),
    path("about/", v.about, name="about"),


    # Shërbimet
    path("services/", v.services_view, name="services"),

    # Projektet (lista + detaje)
    path("projects/", v.project_list, name="projects"),
    path("projects/<slug:slug>/", v.project_detail, name="project_detail"),

    # Kontakt & Kërkesë oferte
    path("contact/", v.contact, name="contact"),
    path("quote/", v.quote, name="quote"),

    # robots.txt për SEO / Google
    path("robots.txt", v.robots_txt, name="robots_txt"),
    path("team/", v.team, name="team"),
path("testimonials/", v.testimonials_page, name="testimonials_page"),
path("page-404/", v.page_404_demo, name="page_404_demo"),

]
