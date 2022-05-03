from django.shortcuts import render, redirect
from .models import IpAddr, PhoneNumber, Room, Message
from django.http import HttpResponse, JsonResponse

def home(request):
    return render(request, 'home.html')


def room(request, room):
    username = request.GET.get('username') # henry
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {

        'username': username,
        'room': room,
        'room_details': room_details,
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    # return HttpResponse("Hi, Message Sent Successfully!!")

def getMessages(request,  room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})

def landing(request):
    return render(request, 'landing.html')

def signup(request):
    return render(request, 'signup.html')

def datasaver(request):
    # taking ip address of the user and storing in the database
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    ip_save = IpAddr.objects.create(ip_addr = ip)
    ip_save.save()

    # saving phone number in the database
    ph = request.POST['phoneNumber']
    ph_save = PhoneNumber.objects.create(phone_number = ph)
    ph_save.save()
    return render(request, 'home.html')