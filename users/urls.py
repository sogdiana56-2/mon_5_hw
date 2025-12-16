from django.urls import path
from .views import RegisterView, SMSCodeConfirm, LoginAPIView
urlpatterns = [
    path("register", RegisterView.as_view()),
    path("login", LoginAPIView.as_view()),
    path('confirm', SMSCodeConfirm.as_view()),
]