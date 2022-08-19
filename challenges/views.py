from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
from django.urls import reverse

monthly_challenges = {
    'january': 'Drink no soda for the entire month',
    'february': 'Walk for at least 20 minutes',
    'march': 'Learn Django for at least 30 minutes daily',
    'april': 'Drink no soda for the entire month',
    'may': 'Walk for at least 20 minutes',
    'june': 'Learn Django for at least 30 minutes daily',
    'july': 'Drink no soda for the entire month',
    'august': 'Walk for at least 20 minutes',
    'september': 'Learn Django for at least 30 minutes daily',
    'october': 'Drink no soda for the entire month',
    'november': 'Walk for at least 20 minutes',
    'december': 'Learn Django for at least 30 minutes daily'
}

def home(request):
    month_list = list(monthly_challenges.keys())
    list_items = ''
    for month in month_list:
        path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href=\'{path}\'>{month.title()}</a></li>'
    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)


def month_by_number(request, month_number):
    month_list = list(monthly_challenges.keys())
    if month_number > len(month_list):
        return HttpResponseNotFound('Invalid month')
    month = month_list[month_number - 1]
    redirect_path = reverse('month-challenge', args=[month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('No challenge for this month yet')
