from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from inventory_app.api.views import CarInventoryList, CarInventoryDetails


urlpatterns=[
    path('list/',CarInventoryList.as_view(),name='car_inventory_list'),
    path('<int:pk>/', CarInventoryDetails.as_view(),name='car_inventory_details')
]