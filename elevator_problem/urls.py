from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ElevatorViewSet, ElevatorRequestViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'elevator', ElevatorViewSet, basename='elevator')
router.register(r'elevator-requests', ElevatorRequestViewSet, basename='elevator_requests')

# router.register(r'elevator/status/', ElevatorViewSet.as_view(), basename='elevator')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]