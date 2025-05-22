from django.urls import path
from .views import HomePageView, contact_view, AboutPageView, OtherWaysToHelpView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # ✅ Ensure `.as_view()` is used
    path('contact/', contact_view, name='contact'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('other-ways-to-help/', OtherWaysToHelpView.as_view(), name='other_ways_to_help'),




]
