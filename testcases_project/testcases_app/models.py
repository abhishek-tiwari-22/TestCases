from django.db import models


class TestCase(models.Model):
    name = models.CharField(max_length=100)
    estimate_time = models.IntegerField()
    module = models.CharField(max_length=100)
    priority = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=[('pass', 'Pass'), ('fail', 'Fail')])

    def __str__(self):
        return self.name
