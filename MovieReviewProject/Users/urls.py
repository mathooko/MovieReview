from .views import CohortViewSet
from rest_framework.routers import DefaultRouter



router= DefaultRouter()
router.register('users', usersViewSet, basename= 'cohort')

urlpatterns = []
urlpatterns += router.urls