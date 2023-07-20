from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add extra responses here
        # FIXME：修复管理站点创建用户时不创建对应userinfo，导致登陆时报错
        data['nickname'] = self.user.userinfo.nickname
        data['groups'] = self.user.groups.values_list('name', flat=True)
        data['permissions'] = self.user.get_all_permissions()
        return data
