from django.urls import path

from .views import CreateLetterAPIView, RandomLetterAPIView


urlpatterns = [
    path("create/letter/", CreateLetterAPIView.as_view(), name="create_letter_url"),
    path("random/letter/", RandomLetterAPIView.as_view(), name="random_letter_url")
]
