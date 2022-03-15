from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.accounts.api.viewset import CreateUserView

router = DefaultRouter()

router.register('users', CreateUserView)

routes = router.urls