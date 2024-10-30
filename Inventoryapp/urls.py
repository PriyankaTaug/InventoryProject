
from django.urls import path
from Inventoryapp.views import Ordercreation, ProductDisplay, ProductEntry, ProductPage

app_name = 'Inventoryapp'
urlpatterns = [
 path('ProductEntry/',ProductEntry.as_view(),name="ProductEntry"),
 path('ProductPage/',ProductPage.as_view()),
 path('ProductDisplay/',ProductDisplay.as_view(),name="ProductDisplay"),
 path('Ordercreation/',Ordercreation.as_view(),name="Ordercreation")
]
