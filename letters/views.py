from rest_framework import views, status
from rest_framework.permissions import AllowAny

from .serializers import LetterModelSerializer
from .models import Letter


class CreateLetterAPIView(views.APIView):
    serializer_class = LetterModelSerializer
    permission_classes = (AllowAny, )

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.data)
        serializer.is_valid(raise_exception=True)
        
