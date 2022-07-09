from django.db import models
from ckeditor.fields import RichTextField


class WeeklyDx(models.Model):
    name = models.CharField(max_length=500)
    img = models.ImageField(upload_to='WeeklyDx')
    body = RichTextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' | ' + str(self.date)

    class Meta:
        verbose_name_plural = 'WEEKLY HEALTH INFORMATION'





class Res(models.Model):
    title = models.CharField(max_length=222)
    img = models.ImageField(upload_to='Recources')
    url = models.URLField(default=None, blank=True, null=True)
    note = RichTextField()


    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'RESOURCES'

class ResImg(models.Model):
    # title = models.CharField(max_length=345)
    img = models.ImageField(upload_to='PANDEMIC/Recources', blank=True)
    img1 = models.ImageField(upload_to='PANDEMIC/Recources', blank=True)
    img2 = models.ImageField(upload_to='PANDEMIC/Recources', blank=True)
    img3 = models.ImageField(upload_to='PANDEMIC/Recources', blank=True)
    res = models.ForeignKey(Res, on_delete=models.CASCADE)


    def __str__(self):
        return f"Onaga"

    class Meta:
        verbose_name_plural = 'RESOURCES IMAGES'



class Testimony(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=66)
    img = models.ImageField(upload_to='Testimony/img', blank=True)
    text = models.TextField()

    def __str__(self):
        return self.name


class FaQ(models.Model):
    question = models.CharField(max_length=222)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Team(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField()
    designation = models.CharField(max_length=250)
    twitter = models.URLField(null=True)
    facebook = models.URLField(null=True)
    instagram = models.URLField(null=True)
    linkedin = models.URLField(null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Email_Sub(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Mailer(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title




