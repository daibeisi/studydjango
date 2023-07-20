from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add extra responses here
        data['nickname'] = self.user.userinfo.nickname if self.user.userinfo else ""
        data['dep_name'] = self.user.userinfo.dep.name if self.user.userinfo.dep else "" if self.user.userinfo else ""
        data['groups'] = self.user.groups.values_list('name', flat=True)
        data['permissions'] = self.user.get_all_permissions()
        return data
