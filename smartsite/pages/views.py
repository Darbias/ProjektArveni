from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .models import Service, Project, Partner, Testimonial
from .forms import ContactForm, QuoteForm


# ==========================
# HOME PAGE
# ==========================
def home(request):
    services = Service.objects.filter(is_active=True)[:6]
    projects = Project.objects.filter(is_featured=True).order_by("-created_at")[:6]
    partners = Partner.objects.filter(is_active=True)[:12]
    testimonials = Testimonial.objects.filter(is_approved=True).order_by("-created_at")[:5]

    # Free Quote në Home
    if request.method == "POST" and request.POST.get("form_id") == "home_quote":
        qform = QuoteForm(request.POST)
        if qform.is_valid():
            obj = qform.save()
            if settings.EMAIL_HOST and settings.EMAIL_HOST_USER:
                try:
                    send_mail(
                        subject=f"[Quote] {obj.name} – {obj.get_service_display()}",
                        message=f"From: {obj.name} <{obj.email}>\nPhone: {obj.phone}\nService: {obj.get_service_display()}\n\n{obj.message}",
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[settings.EMAIL_HOST_USER],
                        fail_silently=True,
                    )
                except Exception:
                    pass
            messages.success(request, "Kërkesa për ofertë u dërgua!")
            return redirect("home")
    else:
        qform = QuoteForm()
        if hasattr(qform, "init_ts"):
            qform.init_ts()

    return render(request, "securex/index.html", {
        "services": services,
        "projects": projects,
        "partners": partners,
        "testimonials": testimonials,
        "quote_form": qform,
    })


# ==========================
# SERVICES
# ==========================
def services_view(request):
    services = Service.objects.filter(is_active=True)
    return render(request, "securex/service.html", {"services": services})


# ==========================
# PROJECTS
# ==========================
def project_list(request):
    qs = Project.objects.order_by("-created_at")
    service_slug = request.GET.get("service")
    if service_slug:
        qs = qs.filter(service__slug=service_slug)
    return render(request, "securex/project_list.html", {"projects": qs})


def project_detail(request, slug):
    project = get_object_or_404(Project.objects.prefetch_related("images"), slug=slug)
    return render(request, "securex/project_detail.html", {"project": project})


# ==========================
# CONTACT PAGE
# ==========================
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            obj = form.save()
            # Dërgo email (nëse SMTP është konfiguruar)
            if settings.EMAIL_HOST and settings.EMAIL_HOST_USER:
                try:
                    send_mail(
                        subject=f"[Contact] {obj.subject} – {obj.name}",
                        message=f"From: {obj.name} <{obj.email}>\nPhone: {obj.phone}\n\n{obj.message}",
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[settings.EMAIL_HOST_USER],
                        fail_silently=True,
                    )
                except Exception:
                    pass
            messages.success(request, "Mesazhi u dërgua me sukses!")
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "securex/contact.html", {"form": form})


# ==========================
# QUOTE PAGE
# ==========================
def quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            obj = form.save()
            if settings.EMAIL_HOST and settings.EMAIL_HOST_USER:
                try:
                    send_mail(
                        subject=f"[Quote] {obj.name} – {obj.get_service_display()}",
                        message=f"From: {obj.name} <{obj.email}>\nPhone: {obj.phone}\nService: {obj.get_service_display()}\n\n{obj.message}",
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[settings.EMAIL_HOST_USER],
                        fail_silently=True,
                    )
                except Exception:
                    pass
            messages.success(request, "Kërkesa për ofertë u dërgua!")
            return redirect("quote")
    else:
        form = QuoteForm()
    return render(request, "securex/quote.html", {"form": form})


# ==========================
# ABOUT PAGE
# ==========================
def about(request):
    ctx = {
        "service_count": Service.objects.filter(is_active=True).count(),
        "project_count": Project.objects.count(),
        "partner_count": Partner.objects.filter(is_active=True).count(),
    }
    return render(request, "securex/about.html", ctx)


# ==========================
# OTHER PAGES / UTILS
# ==========================
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Sitemap: " + request.build_absolute_uri("/sitemap.xml"),
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


# ==========================
# TEAM / TESTIMONIALS / 404 DEMO
# ==========================
def team(request):
    return render(request, "securex/team.html")


def testimonials_page(request):
    items = Testimonial.objects.filter(is_approved=True)
    return render(request, "securex/testimonials.html", {"testimonials": items})

def page_404_demo(request):
    # Thjesht shfaq 404.html si faqe demo (status 200)
    return render(request, "404.html")
