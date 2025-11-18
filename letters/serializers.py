from rest_framework import serializers

from .models import Letter


class LetterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = "__all__"
        read_only_fields = ("country", "state", "ip_address", "created_at")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['all_letter'] = Letter.objects.count()
        return data
