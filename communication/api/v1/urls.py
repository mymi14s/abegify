from rest_framework.routers import DefaultRouter
from .views import WaitlistViewSet, ContactFormViewSet



router = DefaultRouter()
router.register('waitlist', WaitlistViewSet, basename='waitlist')
router.register('contact-form', ContactFormViewSet, basename='contact-form')

urlpatterns = router.urls