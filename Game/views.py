from django.shortcuts import render, render_to_response
from models import Player, Update


class Data():
    pass

def get_home(request):

    data = Data()

    data.playersWaiting = Player.objects.get_players_waiting()
    data.latest = Update.objects.get_latest()
    data.percent = Player.objects.get_percentage_moved()

    return render_to_response("home.html", {
        "data": data,
    })
