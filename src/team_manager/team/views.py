from django.http import HttpResponse
from django.template import loader
from .models import Team
from django.contrib.auth.decorators import login_required


def index(request):
    team_list = Team.objects.all()
    template = loader.get_template("team/team_list.html")
    context = {
        "team_list": team_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def team_detail(request, team_id):
    team = Team.objects.get(id=team_id)
    return HttpResponse("This is the page for %s team." % team.name)
