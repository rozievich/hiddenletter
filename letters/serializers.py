from rest_framework import serializers

from .models import Letter


class LetterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['all_letter'] = instance.all_content
        return data
