from rest_framework import serializers
from . import models
from nxxcgram.images import serializers as images_serializer


class UserProfileSerializer(serializers.ModelSerializer):

    images = images_serializer.CountImageSerializer(many=True, read_only=True)
    following_count: serializers.ReadOnlyField()
    followers_count: serializers.ReadOnlyField()
    post_count: serializers.ReadOnlyField()

    class Meta:
        model = models.User
        fields = (
            'profile_image',
            'username',
            'name',
            'bio',
            'website',
            'post_count',
            'followers_count',
            'following_count',
            'images',

        )


class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'id',
            'profile_image',
            'username',
            'name',
        )
