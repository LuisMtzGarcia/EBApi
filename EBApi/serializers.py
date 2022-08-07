from turtle import title
from rest_framework import serializers

class PropertySerializer(serializers.Serializer):
    """Serializes the properties."""

    public_id =         serializers.CharField()
    title =             serializers.CharField()
    title_image_full =  serializers.URLField()
    title_image_thumb = serializers.URLField()
    location =          serializers.CharField()
    operations =        serializers.JSONField()
    bedrooms =          serializers.IntegerField()
    bathrooms =         serializers.DecimalField(max_digits=5, decimal_places=1)
    parking_spaces =   serializers.IntegerField()
    property_type =     serializers.CharField()
    lot_size =          serializers.DecimalField(max_digits=255, decimal_places=2)
    construction_size = serializers.DecimalField(max_digits=255, decimal_places=2)
    updated_at =        serializers.DateTimeField()
    agent =             serializers.CharField()
    show_prices =       serializers.BooleanField()
    share_commission =  serializers.BooleanField()
