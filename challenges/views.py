from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
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
    'december': None
}


def home(request):
    month_list = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {
        'months': month_list
    })


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
        return render(request, 'challenges/challenge.html', {
            'month': month,
            'text': challenge_text
        })
    except:
        raise Http404()

