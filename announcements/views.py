from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Announcement


@login_required
def announcement_list(request):
    user_role = getattr(request.user, 'role', 'student')
    ann = Announcement.objects.filter(is_active=True).filter(
        target_audience__in=['all', user_role]
    ).exclude(expires_at__lt=timezone.now())
    return render(request, 'announcements/list.html', {'announcements': ann})


@login_required
def create_announcement(request):
    if request.method == 'POST':
        Announcement.objects.create(
            title=request.POST['title'],
            message=request.POST['message'],
            target_audience=request.POST['target_audience'],
            priority=request.POST.get('priority', 'medium'),
            created_by=request.user
        )
        return redirect('announcement_list')
    return render(request, 'announcements/create.html')
