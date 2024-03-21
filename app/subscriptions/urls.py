from django.urls import path
from . import views
urlpatterns = [
    path("", views.SubscriptionList.as_view(), name = 'sub-list'), # api/v1/sub
    path("<int:pk>", views.SubsriptionDetail.as_view(), name = 'sub-detail') # api/v1/sub/<pk>
]