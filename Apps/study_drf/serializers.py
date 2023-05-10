from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework.validators import UniqueValidator

from .models import Snippet, Student, Class


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    highlighted = serializers.ReadOnlyField()

    class Meta:
        model = Snippet
        fields = "__all__"

    def get_owner(self, obj):
        """ 处理自定义的字段 owner, 通过外键获取 UserModel 的数据 """
        return obj.owner.username


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label="账号", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(style={'input_type': 'password'}, label="密码", write_only=True)
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_staff', 'is_active', 'is_superuser',
                  'groups', 'user_permissions']

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"
