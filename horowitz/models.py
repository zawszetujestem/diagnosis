from django.db import models


class Symptoms(models.Model):
    VALUE_ANSWER = (
        (0, "Brak"),
        (1, "Rzadko"),
        (2, "Średnio"),
        (3, "Często")
    )

    symptom = models.CharField(max_length=500, blank=True, null=True)
    answer = models.IntegerField(choices=VALUE_ANSWER, default=0, null=True, blank=True)
    common_symptom = models.BooleanField(default=False)

    def __str__(self):
        return self.symptom


class BoreliaEvents(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    value = models.IntegerField(default=0, blank=True, null=True)
    is_happened = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class HealthCondition(models.Model):
    VALUE_LIST = (
        (1, "0-5 dni"),
        (2, "6-12 dni"),
        (3, "13-20 dni"),
        (4, "21-30 dni")
    )

    name = models.TextField(max_length=500, blank=True, null=True)
    value = models.IntegerField(choices=VALUE_LIST, default=0, null=True, blank=True)

    def __str__(self):
        return self.name
