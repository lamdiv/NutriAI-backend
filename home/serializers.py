from djoser.serializers import UserCreateSerializer
from .models import User


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','name','age','height','weight','email','password')
        