from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
import random


from .models import questionnaire_response, contact_info
from .forms import homepage_confirmation_form, mode_choice_form, final_page_form

def home(request):


    if request.method == 'POST':

        confirmation_status = homepage_confirmation_form(request.POST)
        if confirmation_status.is_valid():
            return redirect('/question1')

    else:

        confirmation_status = homepage_confirmation_form()

    context = {
        "confirmation_status" : confirmation_status
    }
    return render(request, 'poll/home.html',context)



def question1(request):
    #poll = Poll.objects.get(pk=poll_id)

    #Car attributes
    time_car = random.randint(5, 20) #mins
    price_car = random.randint(4, 20) #SAR

    #Bus attributes
    time_bus = random.randint(5, 20) # mins
    time_walk_to_station = random.randint(2, 10) #mins
    time_wait_bus = random.randint(2, 10) #mins
    price_bus = random.randint(2, 5) #SAR

    if request.method == 'POST':

        question1_answer = mode_choice_form(request.POST)
        answer = request.POST.get('mode_choice')

        if question1_answer.is_valid():
            ins = questionnaire_response(time_car = time_car,
                                         price_car = price_car,
                                         time_bus = time_bus,
                                         time_walk_to_station = time_walk_to_station,
                                         time_wait_bus = time_wait_bus,
                                         price_bus = price_bus,
                                         question_answer = answer,
                                         )
            ins.save()
            return redirect('/question2')

    else:
        question1_answer = mode_choice_form()

    context = {
        "question1_answer" : question1_answer,
        "time_car"         : time_car,
        "price_car"        : price_car,
        "time_bus"         : time_bus,
        "time_walk_to_station" : time_walk_to_station,
        "time_wait_bus"        : time_wait_bus,
        "price_bus"            : price_bus,

    }

    return render(request, 'poll/question1.html', context)

def question2(request):
    #poll = Poll.objects.get(pk=poll_id)

    #Car attributes
    time_car = random.randint(5, 20) #mins
    price_car = random.randint(4, 20) #SAR

    #Bus attributes
    time_bus = random.randint(5, 20) # mins
    time_walk_to_station = random.randint(2, 10) #mins
    time_wait_bus = random.randint(2, 10) #mins
    price_bus = random.randint(2, 4) #SAR

    if request.method == 'POST':

        question2_answer = mode_choice_form(request.POST)
        answer = request.POST.get('mode_choice')

        if question2_answer.is_valid():
            ins = questionnaire_response(time_car = time_car,
                                         price_car = price_car,
                                         time_bus = time_bus,
                                         time_walk_to_station = time_walk_to_station,
                                         time_wait_bus = time_wait_bus,
                                         price_bus = price_bus,
                                         question_answer = answer,
                                         )
            ins.save()


        if question2_answer.is_valid():

            return redirect('/final')

    else:
        question2_answer = mode_choice_form()

    context = {
        "question2_answer" : question2_answer,
        "time_car"         : time_car,
        "price_car"        : price_car,
        "time_bus"         : time_bus,
        "time_walk_to_station" : time_walk_to_station,
        "time_wait_bus"        : time_wait_bus,
        "price_bus"            : price_bus,

    }

    return render(request, 'poll/question2.html', context)

def final(request):

    if request.method == 'POST':

        communication_choices = final_page_form(request.POST)
        email_address = request.POST.get('email_address')
        twitter_account = request.POST.get('twitter_account')
        if communication_choices.is_valid():
            ins = contact_info(email_address = email_address, twitter_account = twitter_account)
            ins.save()

            return redirect('/final2')


    else:

        communication_choice = final_page_form()

    context = {
        "communication_choice" : communication_choice,

    }

    return render(request, 'poll/final.html',context)


def final2(request):

    return render(request, 'poll/final2.html')
