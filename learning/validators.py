from rest_framework_simplejwt import serializers
from rest_framework.serializers import ValidationError

from learning.models import Subscription


class YoutubeUrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, attrs):
        url = attrs.get(self.field)
        if url and not url.startswith('https://www.youtube.com/watch?v='):
            raise serializers.ValidationError('Недопустимая ссылка на видео')


class SubscriptionValidator:
    def __call__(self, attrs):
        user = attrs.get('user')
        course = attrs.get('course')
        owner = attrs.get('owner')
        if user and course and owner and Subscription.objects.filter(user=user, course=course, owner=owner).exists():
            raise ValidationError('Вы уже подписаны на этот курс')
