from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="HiddenLetter API",
      default_version='v1',
      description="Hidden Letter - Global letter society",
      terms_of_service="https://github.com/rozievich/hiddenletter",
      contact=openapi.Contact(email="oybekrozievich@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny, )
)


urlpatterns = [
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('swdoc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path("api/v1/", include("letters.urls"))
]
