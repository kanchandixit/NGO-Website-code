from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.utils import timezone



class Slider(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='sliders/')
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class HeroSlider(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='hero_sliders/', blank=True, null=True)
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.CharField(max_length=200, blank=True, null=True, help_text="Use relative URLs like '/donate' or absolute URLs like 'http://example.com'.")

    def __str__(self):
        return self.title
    
class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)  # Add location field
    description = models.TextField()

    def __str__(self):
        return self.name

class DirectorsMessage(models.Model):
    message_text = models.TextField()
    image = models.ImageField(upload_to='director_images/', blank=True, null=True)
    quote = models.TextField(blank=True, null=True)  # Optional motivational quote

    def __str__(self):
        return "Director's Message"


class Gallery(models.Model):
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.category
    
class FocusArea(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='focus_areas/', blank=True, null=True)  # Optional icon for each focus area

    def __str__(self):
        return self.title

class MissionStatement(models.Model):
    title = models.CharField(max_length=255, default="Our Mission")
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Campaign(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    goal_amount = models.FloatField()
    donations_received = models.FloatField(default=0.0)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='campaign_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    # Method to calculate the progress of the campaign
    def calculate_progress(self):
        return round((self.donations_received / self.goal_amount) * 100, 2) if self.goal_amount else 0



class Donation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_id = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, default="Pending")
    created_at = models.DateTimeField(default=timezone.now)  # Set default to current time
    
class GalleryCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    category = models.ForeignKey(GalleryCategory, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    
    
class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_donated = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.user.username} - {self.total_donated}'

class StaticPageContent(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title        
    
class ContactInfo(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField()
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    contact_method = models.CharField(
        max_length=10,
        choices=[('email', 'Email'), ('phone', 'Phone')]
    )
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about_us_images/')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TermsAndConditions(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title           