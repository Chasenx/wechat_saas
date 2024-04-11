from django.http import HttpResponse
from django.shortcuts import render
# from .models import WeChatUser, Status
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from blueapps.account.decorators import login_exempt


# def home(request):
#     return render(request, 'homepage.html')
#

@login_exempt
def show_user(request):
    po = {
        'name': 'woody',
        'motto': 'I love Disney',
        'email': 'woody@disney.com',
        'region': 'Shanghai',
        'pic': 'buzz.png'
    }
    return render(request, 'user.html', {'user': po})


# def show_status(request):
#     statuses = Status.objects.all()
#     return render(request, 'status.html', {'statuses': statuses})
#
#
# def submit_post(request):
#     user = WeChatUser.objects.get(user=request.user)
#     text = request.POST.get('text')
#     if text:
#         status = Status(user=user, text=text)
#         status.save()
#         return redirect('/status')
#     return render(request, 'my_post.html')