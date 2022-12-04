from rest_framework.serializers import ModelSerializer
from cadastro.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserManagerObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token

    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class UserManagerObtainPairView(TokenObtainPairView):
    serializer_class = UserManagerObtainPairSerializer
