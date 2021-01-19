from rest_framework import generics, permissions

from .models import Advert
from .serializers import AdvertListSer, AdvertDetailSer


class AdvertList(generics.ListAPIView):
    """all adds"""
    # permission_classes = [permissions]
    queryset = Advert.objects.all()
    serializer_class = AdvertListSer


class AdvertDetail(generics.RetrieveAPIView):
    """подробно об объявлении"""
    # model = Advert
    queryset = Advert.objects.all()
    lookup_field = 'slug'
    serializer_class = AdvertDetailSer
