from django.contrib import admin
from learning.models import Course, Lesson, Subscription


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'owner',)


@admin.register(Lesson)
class AdminLesson(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'link', 'course', 'owner',)


@admin.register(Subscription)
class AdminSubscription(admin.ModelAdmin):
    list_display = ('user', 'course',)
