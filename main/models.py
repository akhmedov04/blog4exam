from django.db import models
from django.contrib.auth.models import User

class Muallif(models.Model):
    ism =models.CharField(max_length=80)
    yosh=models.PositiveSmallIntegerField()
    kasb=models.CharField(max_length=50)
    user_fk =models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism

class Maqola(models.Model):
    sarlavha=models.CharField(max_length=80)
    mavzu=models.CharField(max_length=80)
    matn=models.TextField()
    sana=models.DateField()
    muallif=models.ForeignKey(Muallif, on_delete=models.CASCADE)
    def __str__(self):
        return self.sarlavha
