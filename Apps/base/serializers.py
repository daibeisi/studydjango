from rest_framework_simplejwt.serializers import TokenObtainSerializer


class DIYTokenObtainSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.name
        return token