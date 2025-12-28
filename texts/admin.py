from django.contrib import admin
from .models import HomeSlide, Announcement, Testimonial, Doctor, ContactInfo, AboutPage

@admin.register(HomeSlide)
class HomeSlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'image']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'subtitle']
    ordering = ['order']

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_editable = ['is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'content']
    date_hierarchy = 'created_at'
    fields = ['title', 'content', 'button_text', 'button_url', 'is_active']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['author', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['quote', 'author']

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialty', 'order', 'is_active']
    list_editable = ['order', 'is_active']

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return ContactInfo.objects.count() == 0
    
@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ['story_title']
    def has_add_permission(self, request):
        # Allow only one instance (singleton)
        return not AboutPage.objects.exists()