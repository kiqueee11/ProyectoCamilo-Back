from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from users.models import CustomUser

class GetUsersView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user = CustomUser

