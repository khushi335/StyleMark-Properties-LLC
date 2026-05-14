from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="index"),
    path("about/",about,name="about"),
    path('services/bathroom-remodeling/', bathroom_remodeling, name='bathroom_remodeling'),
    path('services/kitchen-remodeling/', kitchen_remodeling, name='kitchen_remodeling'),
    path('services/roofing/', roofing, name='roofing'),
    path('services/deck-construction/', deck_construction, name='deck_construction'),
    path('services/full-renovation/', full_renovation, name='full_renovation'),
    path('areas-we-serve/', areas_we_serve, name='areas_we_serve'),
    path('contact/', contact, name='contact'),
]