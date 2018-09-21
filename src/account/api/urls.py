from rest_framework.routers import DefaultRouter
from account.api.views import StudentProfileViewSet, MentorProfileViewSet, UserViewSet

app_name = 'account'

router = DefaultRouter()
router.register(r'student-profile', StudentProfileViewSet, base_name='student-profile')
router.register(r'mentor-profile', MentorProfileViewSet, base_name='mentor-profile')
router.register(r'user', UserViewSet, base_name='user')
urlpatterns = router.urls
