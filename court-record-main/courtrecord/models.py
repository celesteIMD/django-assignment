from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

# Create your models here.

# Evidence and Witnesses are both sources of information that can be used
# by an attorney. They inherit shared attributes from abstract class Source

class Source(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()

    legalUser = models.ForeignKey(User, on_delete=models.CASCADE)
    # 1-many: one user can find many sources.
    # One source can only be found by one user

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Evidence(Source):
    category = models.CharField(max_length=30, blank=True, default="Category")
    icon = models.ImageField(upload_to="media/", blank=True)

class Witness(Source):
    testimony = models.TextField(blank=True, default="Testimony")
    icon = models.ImageField(upload_to="media/", blank=True)

class Battle(models.Model):
    legalUser = models.ManyToManyField(User)
    # Many-to-many: One user can join many battles.
    # One battle can have many users (defense, prosecutor, legal assistant, defendant)

    # Min value is 15 years ago from the current year because that is the
    # statute of limitations on murder in ace attorney
    year = models.IntegerField()

    verdict = models.CharField(max_length=30, blank=True, default="Verdict")

