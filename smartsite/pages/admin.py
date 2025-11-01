from django.contrib import admin
from .models import Service, Project, Partner, Testimonial, ContactMessage, QuoteRequest, ProjectImage

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)

# ✅ Vetëm ky version për ProjectAdmin (me inline fotot)
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "service", "is_featured", "created_at")
    list_filter = ("service", "is_featured")
    search_fields = ("title", "client_name", "location")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProjectImageInline]

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("name",)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("author_name", "rating", "is_approved", "created_at")
    list_filter = ("is_approved", "rating")
    search_fields = ("author_name", "content")

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "service", "created_at")
    list_filter = ("service",)
    search_fields = ("name", "email", "message")
