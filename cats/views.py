from rest_framework import viewsets
from .models import SpyCat, Mission, Target
from .serializers import SpyCatsSerializer, MissionSerializer, TargetSerializer
from rest_framework.exceptions import ValidationError


class SpyCatsViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatsSerializer


class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

    def perform_create(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        target = self.get_object()

        if "notes" in request.data:
            if target.complete or target.mission.complete:
                raise ValidationError(
                    "Cannot update notes because the target or the mission is already completed."
                )

        return super().update(request, *args, **kwargs)


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()
        if mission.spy_cat:
            raise ValidationError(
                "You can't delete mission when it assigned to a SpyCat"
            )

        return super().destroy(request, *args, **kwargs)
