from django.shortcuts import render, render_to_response
from models import Player, Update


class Data():
    pass

def get_home(request):

    data = Data()

    data.playersWaiting = Player.objects.get_players_waiting()
    data.latest = Update.objects.get_latest()
    data.percent = Player.objects.get_percentage_moved()
    if data.latest:
        data.actionMap = data.latest.map_action
        data.presentMap = data.latest.map_state
    if data.latest:
        data.beforeMap = Update.objects.get_before_map(data.latest.id)

    return render_to_response("home.html", {
        "data": data,
    })


def get_archives(request):
    data = Data()

    data.archives = Update.objects.get_archives()

    return render_to_response("archives.html", {
        "data": data,
    })


def get_archive_detail(request, id):
    data = Data()
    data.update = Update.objects.get_by_id(id)

    return render_to_response("archive_detail.html", {
        "data": data,
    })


def get_players(request):
    data = Data()
    data.players = Player.objects.all()

    return render_to_response("players.html", {
        "data": data,
    })