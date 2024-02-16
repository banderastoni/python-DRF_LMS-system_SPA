from django.urls import path

from learning.apps import LearningConfig
from rest_framework.routers import DefaultRouter

from learning.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

app_name = LearningConfig.name


router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='courses')

urlpatterns = [
    path('moto/create/', LessonCreateAPIView.as_view(), name='moto_create'),
    path('moto/', LessonListAPIView.as_view(), name='moto_list'),
    path('moto/<int:pk>/', LessonRetrieveAPIView.as_view(), name='moto_get'),
    path('moto/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='moto_update'),
    path('moto/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='moto_delete'),
] + router.urls

