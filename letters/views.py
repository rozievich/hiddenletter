from rest_framework import views, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.db.models.functions import Random

from .serializers import LetterModelSerializer
from .models import Letter
from .utils import get_user_location



class CreateLetterAPIView(views.APIView):
    serializer_class = LetterModelSerializer
    permission_classes = (AllowAny, )

    @swagger_auto_schema(request_body=LetterModelSerializer)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        
        data = get_user_location(request)
        serializer.save(
            country=data['country'],
            state=data['state'],
            ip_address=data['ip_address']
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RandomLetterAPIView(views.APIView):
    serializer_class = LetterModelSerializer
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        let = Letter.objects.order_by(Random()).first()
        serializer = self.serializer_class(let, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)
