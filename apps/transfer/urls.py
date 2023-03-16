from django.urls import path

#my imports
from .views import CreateTransferView

urlpatterns = [
    path('transfer/', CreateTransferView.as_view(), name = "transfer"),
]
