from calendar import monthrange
from datetime import date, timedelta

from django.shortcuts import redirect, render


def home(request):
    return redirect('weekly_view')


def _get_week_dates(selected_date):
    start_of_week = selected_date - timedelta(days=selected_date.weekday())
    return [start_of_week + timedelta(days=i) for i in range(7)]


def _get_month_grid(year, month):
    weeks = []
    first_day = date(year, month, 1)
    start_day = first_day - timedelta(days=first_day.weekday() + 1 if first_day.weekday() != 6 else 0)
    days_in_month = monthrange(year, month)[1]
    current = start_day
    while len(weeks) < 6:
        week = []
        for _ in range(7):
            week.append({'day': current, 'events': []})
            current += timedelta(days=1)
        weeks.append(week)
        if current.month > month and current.weekday() == 6:
            break
    return weeks


def _build_events():
    return {}


def weekly_view(request):
    today = date.today()
    year = int(request.GET.get('year', today.year))
    month = int(request.GET.get('month', today.month))
    day = int(request.GET.get('day', today.day))
    selected = date(year, month, day)
    week_days = _get_week_dates(selected)
    prev_week = selected - timedelta(days=7)
    next_week = selected + timedelta(days=7)

    context = {
        'selected': selected,
        'week_days': week_days,
        'events_by_date': _build_events(),
        'prev_week': prev_week,
        'next_week': next_week,
    }
    return render(request, 'calendar_app/weekly.html', context)


def monthly_view(request):
    today = date.today()
    year = int(request.GET.get('year', today.year))
    month = int(request.GET.get('month', today.month))
    selected = date(year, month, 1)
    month_grid = _get_month_grid(year, month)

    context = {
        'month': selected.month,
        'year': selected.year,
        'month_name': selected.strftime('%B'),
        'month_grid': month_grid,
        'prev_month': (selected.replace(day=1) - timedelta(days=1)).replace(day=1),
        'next_month': (selected.replace(day=28) + timedelta(days=4)).replace(day=1),
    }
    return render(request, 'calendar_app/monthly.html', context)


def unavailability_view(request):
    return render(request, 'calendar_app/unavailability.html')
