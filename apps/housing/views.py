from django.shortcuts import render, redirect, reverse, HttpResponse, HttpResponseRedirect
from .models import Property
from django.views.generic import ListView, DetailView, View
from apps.housing.models import Property

# Create your views here.
def homepage(request):
    return render(request, "housing/index.html")

def about_us(request):
    return render(request, "housing/about_us.html")

def invest(request):
    return render(request, "housing/invest.html")

class PropertyListView(ListView):
    model = Property

    def get_property_list(request):
        property_listings_qs = Property.objects.all()
        print(property_listings_qs)
        if property_listings.exists():
            property_listings = property_listings_qs.first()
        #print(daily_pick)
        context = {
                'object':property_listings
                }
        print(context)
        return(context)
        return render(request, 'housing/property_list.html', context)
