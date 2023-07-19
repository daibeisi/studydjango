from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['nickname'] = self.user.userinfo.nickname
        data['groups'] = self.user.groups.values_list('name', flat=True)
        data['permissions'] = []  # TODO:查询用户名下所有权限
        return data
