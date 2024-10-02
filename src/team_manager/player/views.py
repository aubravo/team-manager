from django.http import HttpResponse
from django.template import loader
from .models import Player
from django.contrib.auth.decorators import login_required


def index(request):
    player_list = Player.objects.all()
    template = loader.get_template("player/player_list.html")
    context = {
        "player_list": player_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def player_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    return HttpResponse("This is the page for %s player." % str(player))