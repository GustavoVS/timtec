from rest_framework import serializers
from django.contrib.auth import get_user_model


class MoocUserSerializer(serializers.ModelSerializer):
    name = serializers.Field(source='get_full_name')
    picture = serializers.Field(source='get_picture_url')
    is_profile_filled = serializers.BooleanField(source='is_profile_filled')

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'name', 'first_name', 'last_name',
                  'biography', 'picture', 'is_profile_filled')


class MoocUserAdminSerializer(MoocUserSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'name', 'email', 'is_active', 'is_superuser', 'first_name', 'last_name',)


class MoocUserAdminCertificateSerializer(MoocUserSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'name', 'email', 'username')
