from rest_framework import serializers

from backend.gallery.serializers import GallerySer
from .models import *


class CategorySer(serializers.ModelSerializer):
    """Для вывода категорий"""
    class Meta:
        model = Category
        fields = ('name', )


class FilterAdvertSer(serializers.ModelSerializer):
    """Для вывода фильтров"""
    class Meta:
        model = FilterAdvert
        fields = ('name', )


class AdvertListSer(serializers.ModelSerializer):
    """Для вывода списка объявлений"""
    category = CategorySer()
    filters = FilterAdvertSer()
    images = GallerySer()

    class Meta:
        model = Advert
        fields = ('category', 'filters', 'subject', 'images', 'price', 'created', 'slug')


class AdvertDetailSer(serializers.ModelSerializer):
    """Для вывода полного объявления"""
    category = CategorySer()
    filters = FilterAdvertSer()
    images = GallerySer()

    class Meta:
        model = Advert
        fields = ('category', 'filters', 'subject', 'description', 'images', 'file', 'price', 'created','user')