from django.shortcuts import render
from django.conf import settings
import stripe

# Create your views here.
from django.views.generic.base import TemplateView


stripe.api_key = settings.STRIPE_SECRET_KEY

class HomePageView (TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):       
          context = super().get_context_data(**kwargs)        
          context['key'] = settings.STRIPE_PUBLISHABLE_KEY        
          return context
    
def success(request):
     if request.method == 'POST':
          charge=stripe.Charge.create(
               amount=500,
               currency='usd',
               description='Payment Gateway',
               source=request.POST['stripeToken']
          )
          return render(request,'success.html')