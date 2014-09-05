from django.shortcuts import render, render_to_response

def get_home(request):
    return render_to_response("base.html")
