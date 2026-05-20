from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Grab data directly from the HTML input name="" attributes
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Simple validation check to ensure everything was filled out
        if name and email and subject and message:
            
            # Email layout sent to you/admin
            admin_message = f"""
New Style Mark Properties Inquiry:

Name: {name}
Email: {email}
Service Needed: {subject}

Project Details:
{message}
"""

            # Email notification sent to the client
            customer_message = f"""
Hi {name},

Thank you for reaching out to Style Mark Properties LLC! 

We have received your request regarding "{subject}". Our team will review the details of your project and get back to you shortly.

Your Details:
Service: {subject}
Message:
{message}

Best regards,

The Style Mark Properties LLC Team
"""

            try:
                # 1. Send notice to the admin list
                send_mail(
                    subject=f"New Web Inquiry – {subject}",
                    message=admin_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=settings.ADMIN_EMAIL,
                    fail_silently=False,
                )

                # 2. Send confirmation auto-responder to customer
                send_mail(
                    subject="We've received your inquiry - Style Mark Properties LLC",
                    message=customer_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],
                    fail_silently=False,
                )

                messages.success(request, "Your message has been sent successfully!")
                
                # Append '#contact' onto the view name loop redirect
                return redirect('/#contact') 

            except Exception as e:
                # Prints terminal trace if your server's .env SMTP credentials fail authorization
                print("Email Configuration Error Error Details:", e)
                messages.error(request, "There was an error sending your message. Please try again later.")
                return redirect('/#contact')
        else:
            messages.error(request, "Please fill out all required fields correctly.")
            return redirect('/#contact')

    # Handles the normal GET request when visiting the page initially
    return render(request, "main/index.html")
    
def about(request):
    return render(request,"main/about.html")

def bathroom_remodeling(request):
    return render(request, 'main/bathroom-remodeling.html')
    
def kitchen_remodeling(request):
    return render(request, 'main/kitchen-remodeling.html')
    
def roofing(request):
    return render(request, 'main/roofing_services.html')
    
def deck_construction(request):
    return render(request, 'main/deck_construction.html')
    
def full_renovation(request):
    return render(request, 'main/full_renovation.html')
    
def areas_we_serve(request):
    return render(request, 'main/areas-we-serve.html')

def contact(request):
    if request.method == 'POST':
        # Grab data directly from your new HTML input name="" attributes
        name = request.POST.get('name')
        email = request.POST.get('email')
        service_raw = request.POST.get('service')
        message = request.POST.get('message')

        # Clean up dropdown values for the email display
        service_mapping = {
            'general': 'General Inquiry',
            'remodeling': 'Remodeling',
            'roofing': 'Roofing',
            'maintenance': 'Maintenance'
        }
        service_clean = service_mapping.get(service_raw, 'General Inquiry')

        # Ensure all required fields are present
        if name and email and service_clean and message:
            
            # Formatted email sent to the Admin team
            admin_message = f"""
New Style Mark Properties Inquiry:

Name: {name}
Email: {email}
Service Needed: {service_clean}

Project Details:
{message}
"""

            # Auto-responder email sent to the potential client
            customer_message = f"""
Hi {name},

Thank you for reaching out to Style Mark Properties LLC! 

We have received your request regarding "{service_clean}". Our team will review the details of your project and get back to you shortly.

Your Details:
Service Requested: {service_clean}
Message Provided:
{message}

Best regards,

The Style Mark Properties LLC Team
"""

            try:
                # 1. Send notice alert email to the admin addresses
                send_mail(
                    subject=f"New Web Inquiry – {service_clean}",
                    message=admin_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=settings.ADMIN_EMAIL,
                    fail_silently=False,
                )

                # 2. Send confirmation auto-responder email copy to customer
                send_mail(
                    subject="We've received your inquiry - Style Mark Properties LLC",
                    message=customer_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],
                    fail_silently=False,
                )

                messages.success(request, "Your message has been sent successfully!")
                return redirect('/contact/#contact-form') # Redirection path with smooth snap anchor jump

            except Exception as e:
                # Prints explicit debug text inside the host terminal console if settings fail authorization
                print("SMTP Email Configuration Link Error:", e)
                messages.error(request, "There was an error sending your message. Please try again later.")
                return redirect('/contact/#contact-form')
        else:
            messages.error(request, "Please fill out all required fields correctly.")
            return redirect('/contact/#contact-form')

    # Handles the normal initial GET load
    return render(request, 'main/contact.html')