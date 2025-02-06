from django.contrib import admin
from .models import Slider, Event, DirectorsMessage, Gallery, FocusArea, MissionStatement, Campaign, GalleryCategory, GalleryImage, StaticPageContent
from django.contrib.auth.models import User
from .models import Donor, StaticPageContent, Slider, HeroSlider, ContactInfo, ContactSubmission, AboutUs,TermsAndConditions


# admin.site.register(Slider)
# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     list_display = ('name', 'date', 'location')
#     search_fields = ('name', 'location')

@admin.register(DirectorsMessage)
class DirectorsMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'message_text', 'quote')
    search_fields = ('message_text', 'quote')

admin.site.register(Gallery)

admin.site.register(FocusArea)

@admin.register(MissionStatement)
class MissionStatementAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ['title', 'goal_amount', 'start_date', 'end_date']
    search_fields = ['title']

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    search_fields = ['title', 'category__name']
    list_filter = ['category']

admin.site.register(GalleryCategory)
admin.site.register(GalleryImage, GalleryImageAdmin)    


class CustomAdminSite(admin.AdminSite):
    site_header = 'NGO Admin Dashboard'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name='dashboard'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        # You can fetch the statistics you need for the dashboard here
        total_campaigns = Campaign.objects.count()
        total_gallery_images = GalleryImage.objects.count()
        total_events = Event.objects.count()
        total_users = User.objects.count()

        context = {
            'total_campaigns': total_campaigns,
            'total_gallery_images': total_gallery_images,
            'total_events': total_events,
            'total_users': total_users,
        }
        return render(request, 'admin/dashboard.html', context)

# Register the custom admin site
admin_site = CustomAdminSite(name='custom_admin')
admin_site.register(Campaign)
admin_site.register(GalleryCategory)
admin_site.register(GalleryImage)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location')  # Display location in admin list view
    fields = ('name', 'date', 'location', 'description') 

# admin.site.register(Event, EventAdmin)
admin_site.register(StaticPageContent)
admin_site.register(User)

class DonorAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_donated')
    search_fields = ('user__username',)

admin.site.register(Donor, DonorAdmin)

class StaticPageContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)

admin.site.register(StaticPageContent, StaticPageContentAdmin)

class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'url')
    search_fields = ('title',)

admin.site.register(Slider, SliderAdmin)

@admin.register(HeroSlider)
class HeroSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'button_text', 'button_link')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')    

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email')
    list_filter = ('submitted_at',)    

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)    

@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)    