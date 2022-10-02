from django.urls import path 
from .views import BookAPIView

# Create your views here.
urlpatterns = [
    path('', BookAPIView.as_view()),
]
