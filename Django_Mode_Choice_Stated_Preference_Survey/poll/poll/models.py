from django.db import models
from django import forms

# class homepage_confirmation(models.Model):
#     confirmation = models.BooleanField(widget=forms.CheckboxInput, default=False)

class questionnaire_response(models.Model):

    time_car             = models.IntegerField(default = 0) #mins
    price_car            = models.IntegerField(default = 0) #SAR
    time_bus             = models.IntegerField(default = 0) # mins
    time_walk_to_station = models.IntegerField(default = 0) #mins
    time_wait_bus        = models.IntegerField(default = 0) #mins
    price_bus            = models.IntegerField(default = 0) #SAR
    mode_answers = (('Bus','Bus'),('Car','Car'))
    question_answer = models.CharField(max_length=3, choices=mode_answers, default = "Nul")


class contact_info(models.Model):
    email_address    = models.EmailField()
    twitter_account  = models.CharField(max_length = 30)
    #creation_date = models.DateTimeField(default=timezone.now)
