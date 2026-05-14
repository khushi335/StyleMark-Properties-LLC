from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"main/index.html")
    
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
        # Logic to handle form (send email or save to DB)
        pass
    return render(request, 'main/contact.html')