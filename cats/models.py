from django.db import models
import uuid

class SpyCat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=258)
    years_of_exp = models.IntegerField()
    breed = models.CharField(max_length=128)
    salary = models.DecimalField(decimal_places=5, max_digits=10)

    def __str__(self):
        return self.name

class Mission(models.Model):
    spy_cat = models.ForeignKey(SpyCat, related_name="missions", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Target(models.Model):
    mission = models.ForeignKey(Mission, related_name="targets", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    notes = models.TextField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name