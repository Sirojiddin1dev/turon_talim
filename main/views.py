from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from .models import Banner
from .serializers import BannerListSerializer

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerListSerializer

    @swagger_auto_schema(
        operation_summary="Barcha bannerlarni olish",
        operation_description="Ushbu endpoint barcha mavjud bannerlarni JSON ko‘rinishida qaytaradi.",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)