from django.urls import path
from .views import HomePageView  # ✅ Correct import

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # ✅ Ensure `.as_view()` is used
]
