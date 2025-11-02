from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Service(models.Model):
    icon = models.CharField(
        max_length=50, blank=True,
        help_text="Bootstrap Icon p.sh. 'bi-camera-video' ose 'bi-fingerprint'"
    )
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    icon_class = models.CharField(max_length=80, blank=True, help_text="p.sh. 'bi bi-camera-video'")
    short_description = models.CharField(max_length=255, blank=True)
    long_description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)  # ✅ shtuar për uniformitet
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    



class Project(models.Model):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    client_name = models.CharField(max_length=160, blank=True)
    location = models.CharField(max_length=160, blank=True)
    description = models.TextField(blank=True)
    cover = models.ImageField(upload_to="projects/covers/", blank=True, null=True)
    completed_on = models.DateField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)  # ✅ ndryshuar nga auto_now_add për të shmangur gabime

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Partner(models.Model):
    name = models.CharField(max_length=140)
    website_url = models.URLField(blank=True)
    logo = models.ImageField(upload_to="partners/logos/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    photo = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    author_name = models.CharField(max_length=120)
    author_role = models.CharField(max_length=120, blank=True)
    rating = models.PositiveSmallIntegerField(default=5)
    content = models.TextField()
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.author_name} ({self.rating}/5)"


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=60, blank=True)
    subject = models.CharField(max_length=160)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"[Contact] {self.name} – {self.subject}"


SERVICE_CHOICES = [
    ("cctv", "CCTV / Kamera Sigurie"),
    ("alarm", "Sisteme Alarmi"),
    ("access", "Kontroll Aksesi"),
    ("smarthome", "Smart Home / Automatizim"),
]


class QuoteRequest(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=60, blank=True)
    service = models.CharField(max_length=40, choices=SERVICE_CHOICES, default="cctv")
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"[Quote] {self.name} – {self.get_service_display()}"

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="projects/gallery/")
    caption = models.CharField(max_length=180, blank=True)

    def __str__(self):
        return f"{self.project.title} – image"
