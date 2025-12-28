from django.db import models

class HomeSlide(models.Model):
    # Main content
    image = models.ImageField(upload_to='slides/')  # images will be saved in media/slides/
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True, null=True)

    # Control order & visibility
    order = models.PositiveSmallIntegerField(default=0, help_text="Lower number = appears first")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide this slide")

    class Meta:
        ordering = ['order']
        verbose_name = "Home Slide"
        verbose_name_plural = "Home Slides"

    def __str__(self):
        return f"{self.title} (order {self.order})"


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    button_text = models.CharField(max_length=100, default="Learn More", blank=True)
    button_url = models.CharField(max_length=200, default="/contact/", blank=True)
    is_active = models.BooleanField(default=True, help_text="Check to show this announcement")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # newest first
        verbose_name_plural = "Announcements"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Optional: if you want only one active at a time (uncomment if desired)
        # if self.is_active:
        #     Announcement.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


class Testimonial(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.author} - {self.quote[:40]}..."


class Doctor(models.Model):
    photo = models.ImageField(upload_to='doctors/')
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    phone = models.CharField(max_length=20)
    emergency_phone = models.CharField(max_length=20)
    address = models.TextField()
    logo = models.ImageField(upload_to='footer/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Contact Info"

    def __str__(self):
        return "Contact Information"

    def save(self, *args, **kwargs):
        self.pk = 1  # enforce singleton
        super().save(*args, **kwargs)
        
        
class AboutPage(models.Model):
    hero_background = models.ImageField(upload_to='about/', help_text="Background image for the hero section")
    story_image = models.ImageField(upload_to='about/', help_text="Image next to 'Our Story' section")
    story_title = models.CharField(max_length=200, default="Our Story")
    story_content = models.TextField(help_text="The main story text for the About page")

    def __str__(self):
        return "About Page Content"

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"
        
