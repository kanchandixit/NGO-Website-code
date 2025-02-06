from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    # path('campaigns/', views.campaigns, name='campaigns'),
    # path('get_involved/', views.get_involved, name='get_involved'),
    path('contact/', views.contact_submission, name='contact'),
    path('contact/', views.contact_submission, name='contact_submission'),
    path('get-involved/', views.get_involved, name='get_involved'),
    path('events/', views.events, name='events'),
    path('donate/', views.donate, name='donate'),
    path('join-us/', views.join_us, name='join_us'),
    # path('campaigns/create/', views.campaign_create, name='campaign_create'),
    path('donate/campaign/<int:campaign_id>/', views.donate_to_campaign, name='donate_campaign'),

    path('campaigns/', views.campaigns, name='campaign_list'),  # Ensure this matches 'campaign_list'
    
    # Other URL patterns...
    # path('donate/<int:campaign_id>/', views.donate_to_campaign, name='donate'),
    path('gallery/', views.gallery, name='gallery'), 
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),

    path("payment-success/", views.payment_success, name="payment_success"),
    
]
