from rest_framework import serializers
from .models import SpyCat, Target, Mission
import requests
from rest_framework.exceptions import ValidationError


class SpyCatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ["id", "name", "years_of_exp", "breed", "salary"]

    def validate_breed(self, value):
        api_data = requests.get(f"https://api.thecatapi.com/v1/breeds/{value}")

        if api_data.status_code != 200:
            raise ValidationError("This breed is not maintains")

        return value


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ["name", "notes", "country", "complete", "id", "mission"]


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)
    spy_cat = serializers.PrimaryKeyRelatedField(queryset=SpyCat.objects.all())

    class Meta:
        model = Mission
        fields = ["id", "name", "description", "complete", "spy_cat", "targets"]

    def create(self, validated_data):
        targets_data = validated_data.pop("targets")
        spy_cat = validated_data.pop("spy_cat")

        mission = Mission.objects.create(spy_cat=spy_cat, **validated_data)

        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)

        return mission
