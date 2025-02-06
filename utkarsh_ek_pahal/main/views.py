from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import razorpay, json
from django.utils.timezone import now
from django.http import JsonResponse
from decimal import Decimal
from django.contrib import messages
from django.urls import reverse
from .models import (
    DirectorsMessage, Event, FocusArea, MissionStatement, 
    Campaign, GalleryCategory, GalleryImage, HeroSlider, 
    ContactInfo, ContactSubmission, AboutUs, TermsAndConditions, Donation
)
from .forms import DonationForm, CampaignForm, ContactSubmissionForm

razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def home(request):
    events = Event.objects.all().order_by('date')  # Fetch events
    directors_message = DirectorsMessage.objects.first()  # Fetch the first (or only) message
    focus_areas = FocusArea.objects.all()  # Fetch focus areas
    mission = MissionStatement.objects.first()
    hero_sliders = HeroSlider.objects.all()
    return render(request, 'main/home.html', {
        'hero_sliders': hero_sliders,
        'events': events,
        'directors_message': directors_message,
        'focus_areas': focus_areas,
        'mission': mission
    })

def about(request):
    about_content = AboutUs.objects.first()  # Get the first AboutUs entry
    return render(request, 'main/about.html', {'about_content': about_content})

def gallery(request):
    categories = GalleryCategory.objects.all()
    gallery = {category.name: GalleryImage.objects.filter(category=category) for category in categories}
    return render(request, 'main/gallery.html', {'gallery': gallery})

def get_involved(request):
    return render(request, 'get_involved.html')

def events(request):
    upcoming_events = Event.objects.filter(date__gte=now().date()).order_by('date')  # Fetch only today's and future events
    return render(request, 'events.html', {'events': upcoming_events})


def join_us(request):
    return render(request, 'join_us.html')


def campaigns(request):
    all_campaigns = Campaign.objects.all()
    
    context = {
        'campaigns': [
            {
                'id': campaign.id,
                'title': campaign.title,
                'description': campaign.description,
                'goal_amount': campaign.goal_amount,
                'achieved': campaign.donations_received,
                'progress': campaign.calculate_progress(),
                'start_date': campaign.start_date,
                'end_date': campaign.end_date,
                'image_url': campaign.image.url if campaign.image else None,
                'donation_url': reverse('donate_campaign', args=[campaign.id]),
            }
            for campaign in all_campaigns
        ]
    }

    return render(request, 'main/campaign_list.html', context)

def campaign_detail(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    return render(request, 'main/campaign_detail.html', {'campaign': campaign})

def contact_submission(request):
    if request.method == 'POST':
        form = ContactSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your message! We will get back to you soon.")
            return redirect('contact')  # Adjust as per your URL pattern
        else:
            messages.error(request, "There was an error with your submission. Please try again.")
    else:
        form = ContactSubmissionForm()

    contact_details = ContactInfo.objects.all()
    return render(request, 'main/contact.html', {
        'form': form,
        'contact_details': contact_details
    })

def terms_and_conditions(request):
    terms = TermsAndConditions.objects.first()  # Fetch the first entry
    return render(request, 'main/terms_and_conditions.html', {'terms': terms})

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError("Type not serializable")

def donate(request):
    if request.method == 'POST':
        
        try:
            amount = request.POST.get('amount')
            if amount is None:
                raise ValueError("Amount is required.")

            # Ensure the amount is a Decimal
            amount = Decimal(amount)  # Convert to Decimal for accuracy
            print(f"Cleaned amount from form: {amount}")

            # # Convert amount to paise (integer value)
            amount_in_paise = int(amount * 100)  # Convert Decimal to integer
            print(f"Amount in paise for Razorpay: {amount_in_paise}")

            # Create Razorpay order
            data = {
                "amount": amount_in_paise,  # Amount in paise
                "currency": "INR",
                "payment_capture": 1  # Auto capture payment
            }
            print(f"Razorpay order data: {data}")
            order = razorpay_client.order.create(data=data)
            print(order)
            # Save donation record
            donation = Donation.objects.create(
                amount=amount,
                order_id=order['id']
            )
            donation.save()

            # Render payment confirmation page
            return render(request, "main/confirm_payment.html", {
                "order_id": order['id'],
                "amount": amount,
                "razorpay_key_id": settings.RAZORPAY_KEY_ID,
                "donation_id": donation.id
            })
        except Exception as e:
            print(e)
            messages.error(request, f"Error in payment creation: {e}")
            return redirect('donate')

    return render(request, 'main/donate.html')



# Handling successful payment notification from Razorpay
@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            payment_id = data.get("razorpay_payment_id")
            donation_id = data.get("donation_id")

            # Find the corresponding donation record
            donation = Donation.objects.get(id=donation_id)
            donation.payment_id = payment_id
            donation.status = "Success"
            donation.save()

            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "failed", "error": str(e)})

    return JsonResponse({"status": "failed", "error": "Invalid request method."})

def donate_to_campaign(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    return render(request, 'main/donate.html', {'campaign': campaign})

