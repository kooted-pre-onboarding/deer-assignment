from django.urls import path
from .views import UseView

urlpatterns = [
    path('', UseView.as_view()),
]
